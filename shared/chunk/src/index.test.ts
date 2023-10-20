import chunk from ".";

describe("chunk", () => {
  it("should return an empty array when given an empty array", () => {
    const input: number[] = [];
    const result = chunk(input);
    expect(result).toEqual([]);
  });

  it("should return an array with one chunk when given an array with one element", () => {
    const input = [1];
    const result = chunk(input);
    expect(result).toEqual([[1]]);
  });

  it("should return an array with two chunks when given an array with two elements", () => {
    const input = [1, 2];
    const result = chunk<number>(input);
    expect(result).toEqual([[1, 2]]);
  });

  it("should return an array with two chunks when given an array with three elements", () => {
    const input = [1, 2, 3];
    const result = chunk<number>(input);
    expect(result).toEqual([[1, 2], [3]]);
  });

  it("should return an array with three chunks when given an array with four elements", () => {
    const input = [1, 2, 3, 4];
    const result = chunk<number>(input);
    expect(result).toEqual([
      [1, 2],
      [3, 4],
    ]);
  });

  it("should return an array with three chunks when given an array with five elements and a chunk size of 2", () => {
    const input = [1, 2, 3, 4, 5];
    const result = chunk<number>(input, 2);
    expect(result).toEqual([[1, 2], [3, 4], [5]]);
  });

  it("should return an array with two chunks when given an array with five elements and a chunk size of 3", () => {
    const input = [1, 2, 3, 4, 5];
    const result = chunk<number>(input, 3);
    expect(result).toEqual([
      [1, 2, 3],
      [4, 5],
    ]);
  });
});
