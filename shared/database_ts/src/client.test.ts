import { describe, it, beforeAll, expect, jest } from "@jest/globals";
import DatabaseClient from "./client";

const clientMock = {
  connect: jest.fn(),
  query: jest.fn(),
  end: jest.fn(),
};

jest.mock("pg", () => {
  return {
    Client: jest.fn(() => clientMock),
  };
});

type User = {
  id: number;
  name: string;
  email: string;
};

const users: User[] = [
  { id: 1, name: "John Doe", email: "johndoe@me.com" },
  { id: 2, name: "Jane Doe", email: "janedoe@me.com" },
];

describe("DatabaseClient", () => {
  let client: DatabaseClient;

  beforeAll(() => {
    clientMock.query.mockClear();
    client = new DatabaseClient();
  });

  it("should execute a SQL query", async () => {
    clientMock.query.mockReturnValue(Promise.resolve({ rows: users }));

    const query = "SELECT * FROM users";
    const result = await client.sql<User>(query, []);

    expect(Array.isArray(result)).toBe(true);
    expect(result.length).toBeGreaterThan(0);

    expect(result[0]).toHaveProperty("id");
    expect(result[0]).toHaveProperty("name");
    expect(result[0]).toHaveProperty("email");
  });
});
