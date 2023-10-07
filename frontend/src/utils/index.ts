import { DomainsResponse } from "@/utils/types";

export const getData = async (
  page: number = 1,
  search: string = ""
): Promise<DomainsResponse> => {
  const res = await fetch(`/api?page=${page}&search=${search}`, {
    cache: "no-store",
  });

  return res.json();
};
