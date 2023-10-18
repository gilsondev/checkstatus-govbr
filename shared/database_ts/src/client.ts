import { Client } from "pg";

export class DatabaseClient {
  client: Client;

  constructor() {
    this.client = new Client({
      connectionString: process.env.DATABASE_URL,
      keepAlive: true,
      keepAliveInitialDelayMillis: 30000,
    });
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
