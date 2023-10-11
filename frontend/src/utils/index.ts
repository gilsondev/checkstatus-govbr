import { DomainsResponse } from "@/utils/types";

export const getData = async (page: number = 1): Promise<DomainsResponse> => {
  const res = await fetch(`/api?page=${page}`, {
    cache: "no-store",
  });

  return res.json();
};

export const searchData = async (search: string): Promise<DomainsResponse> => {
  const res = await fetch(`/api?search=${search}`, {
    cache: "no-store",
  });

  return res.json();
};
