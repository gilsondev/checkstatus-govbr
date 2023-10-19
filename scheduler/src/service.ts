import { createClient } from "@checkstatusgovbr/database-ts";
import { DatabaseClient } from "@checkstatusgovbr/database-ts/src/client";
import AvailabilityDomains from "./availability";
import pino from "pino";
import { Domain } from "domain";

const logger = pino();

export type DomainData = {
  domain: string;
  available: boolean;
};

export default class AvailabilityDomainsService {
  client: DatabaseClient;
  pingClient: AvailabilityDomains;

  constructor() {
    this.client = createClient();
    this.pingClient = new AvailabilityDomains();
  }

  private async fetchDomains(): Promise<DomainData[]> {
    try {
      logger.info("Fetching domains");
      const result = await this.client.sql<DomainData>(
        "SELECT domain FROM domains",
        []
      );
      return result;
    } catch (error) {
      logger.error(error);
    } finally {
      await this.client.close();
    }

    return [];
  }

  async pingDomains() {
    const domains = await this.fetchDomains();

    let results: DomainData[] = [];
    for (const data of domains) {
      logger.info(`Pinging ${data.domain}`);
      const isAvailable = await this.pingClient.isAvailable(data.domain);

      logger.info(
        `Domain ${data.domain} is ${
          isAvailable ? "available" : "not available"
        }`
      );
      results.push({ ...data, available: isAvailable });
    }

    await this.updateDomainsStatus(results);
  }

  public async updateDomainsStatus(domains: DomainData[]) {
    const updateValues = domains
      .map((data) => `('${data.domain}', ${data.available}, NOW())`)
      .join(", ");

    logger.info(`Updating domains`);
    try {
      this.client = createClient();
      await this.client.rawSQL<DomainData>(
        `UPDATE domains SET available = v.available, updated_at = v.updated_at FROM (VALUES ${updateValues}) AS v(domain, available, updated_at) WHERE domains.domain = v.domain`
      );

      logger.info(`Updated ${domains.length} domains`);
    } catch (error) {
      logger.error(error);
    } finally {
      logger.debug("Closing connection");
      await this.client.close();
    }
  }
}
