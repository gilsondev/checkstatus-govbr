import { DomainsResponse, FilterSearch } from "@/utils/types";

export const getData = async (
  page: number = 1,
  filter: FilterSearch | null
): Promise<DomainsResponse> => {
  const filterParams = createFilterParams(filter) || "";
  const res = await fetch(`/api?page=${page}&${filterParams}`, {
    cache: "no-store",
  });

  return res.json();
};

export const searchData = async (
  search: string,
  page: number = 1,
  filter: FilterSearch | null
): Promise<DomainsResponse> => {
  const filterParams = createFilterParams(filter);

  const res = await fetch(
    `/api?search=${search}&page=${page}&${filterParams}`,
    {
      cache: "no-store",
    }
  );

  return res.json();
};
const createFilterParams = (filter: FilterSearch | null): string => {
  let filterParams = "";
  if (filter) {
    filterParams = new URLSearchParams({
      available: filter.available.toString(),
      status: filter.status,
    }).toString();
  }
  return filterParams;
};
