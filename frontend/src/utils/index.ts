import { DomainsResponse } from "@/utils/types";

export const getData = async (page: number = 1): Promise<DomainsResponse> => {
  const res = await fetch(`/api?page=${page}`, {
    cache: "no-store",
  });

  return res.json();
};

export const searchData = async (
  search: string,
  page: number = 1
): Promise<DomainsResponse> => {
  const res = await fetch(`/api?search=${search}&page=${page}`, {
    cache: "no-store",
  });

  return res.json();
};
