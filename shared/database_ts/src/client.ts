import { Client } from "pg";

export class DatabaseClient {
  client: Client;

  constructor() {
    this.client = new Client(process.env.DATABASE_URL);
    this.client.connect();
  }

  async sql<T>(query: string, values: any[]) {
    const result = await this.client.query(query, values);
    return result.rows.map((row: T) => row);
  }

  async close() {
    await this.client.end();
  }
}
