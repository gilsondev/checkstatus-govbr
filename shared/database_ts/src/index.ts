import { DatabaseClient } from "./client";

const createClient = () => {
  return new DatabaseClient();
};

export { createClient };
