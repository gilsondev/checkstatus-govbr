const chunk = <T>(collection: T[], size: number = 2): T[][] => {
  const result: T[][] = [];

  for (let start = 0; start < collection.length; start += size) {
    let end = start + size;
    result.push(collection.slice(start, end));
  }
  return result;
};

export default chunk;
