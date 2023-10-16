import { createClient } from "@checkstatusgovbr/database-ts";
import { DatabaseClient } from "@checkstatusgovbr/database-ts/src/client";
import AvailabilityDomains from "./availability";
import pino from "pino";

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

  async pingDomains() {
    logger.info("Pinging domains");
    const domains = await this.client.sql<DomainData>(
      "SELECT domain FROM domains",
      []
    );

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

    const updateValues = results
      .map((data) => `('${data.domain}', ${data.available})`)
      .join(", ");

    await this.client.sql<DomainData>(
      `UPDATE domains SET available = v.available FROM (VALUES ${updateValues}) AS v(domain, available) WHERE domains.domain = v.domain`,
      []
    );

    logger.info(`Updated ${results.length} domains`);
  }
}
