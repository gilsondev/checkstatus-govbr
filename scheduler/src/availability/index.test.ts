import { jest, describe, it, beforeEach, expect } from "@jest/globals";
import axios from "axios";
import AvailabilityDomains from ".";

jest.mock("axios");
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe("AvailabilityDomains", () => {
  let availabilityDomains: AvailabilityDomains;

  beforeEach(() => {
    mockedAxios.mockClear();
    availabilityDomains = new AvailabilityDomains();
  });

  describe("isAvailable", () => {
    const parametrizedTests = [
      {
        domain: "www.google.com",
        status: 200,
        result: true,
      },
      {
        domain: "www.google.com",
        status: 302,
        result: true,
      },
      {
        domain: "www.google.com",
        status: 404,
        result: true,
      },
      {
        domain: "www.google.com",
        status: 500,
        result: false,
      },
    ];

    parametrizedTests.forEach((test) => {
      it(`should return ${test.result} if the status code is ${test.status}`, async () => {
        mockedAxios.head.mockResolvedValue({
          status: test.status,
        });

        const result = await availabilityDomains.isAvailable(test.domain);
        expect(result).toBe(test.result);
      });
    });

    it("should return false if raise error", async () => {
      mockedAxios.head.mockRejectedValue(new Error("timeout"));

      const result = await availabilityDomains.isAvailable("www.google.com");
      expect(result).toBe(false);
    });
  });
});
