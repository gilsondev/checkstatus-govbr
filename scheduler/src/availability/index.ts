import axios from "axios";

export default class AvailabilityDomains {
  private async isAvailableWithProtocol(
    domain: string,
    protocol: string
  ): Promise<boolean> {
    try {
      const url = `${protocol}://${domain}`;
      const resp = await axios.head(url, {
        timeout: 5000,
        validateStatus: () => true,
      });

      return resp.status >= 200 && resp.status < 500;
    } catch (error) {
      return false;
    }
  }

  async isAvailable(domain: string): Promise<boolean> {
    const isAvailableHttp = await this.isAvailableWithProtocol(domain, "http");
    if (isAvailableHttp) {
      return true;
    }
    return this.isAvailableWithProtocol(domain, "https");
  }
}
