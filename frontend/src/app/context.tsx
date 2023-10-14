import React, { createContext } from "react";
import { DomainsResponse, FilterSearch } from "../utils/types";
import { getData, searchData } from "../utils";
import { useDebounce } from "usehooks-ts";
import { useRouter } from "next/navigation";

export type DomainContextType = {
  getDomains: (page: number, filters: FilterSearch) => void;
  searchDomains: (search: string, page: number, filter: FilterSearch) => void;
  setLoading: (isLoading: boolean) => void;
  setPage: (page: number) => void;
  setSearchTerm: (searchTerm: string) => void;
  setFilter: (filter: FilterSearch) => void;
  isLoading: boolean;
  page: number;
  searchTerm: string;
  filter: FilterSearch;
  domains: DomainsResponse;
};

const defaultDomainsValue = {
  items: [],
  total: 0,
  page: 0,
  size: 0,
  pages: 0,
};

export const DomainContext = createContext<DomainContextType>({
  getDomains: () => {},
  searchDomains: () => {},
  setLoading: () => {},
  setPage: () => {},
  setSearchTerm: () => {},
  setFilter: () => {},
  page: 1,
  searchTerm: "",
  isLoading: true,
  filter: { available: "", status: "" },
  domains: defaultDomainsValue,
});

const DomainProvider = ({ children }: { children: React.ReactNode }) => {
  const router = useRouter();

  const [isLoading, setLoading] = React.useState(true);
  const [page, setPage] = React.useState<number>(1);
  const [searchTerm, setSearchTerm] = React.useState<string>("");
  const [filter, setFilter] = React.useState<FilterSearch>({
    available: "",
    status: "",
  });
  const [domains, setDomains] =
    React.useState<DomainsResponse>(defaultDomainsValue);

  const debounceValue = useDebounce<string>(searchTerm, 500);

  const getDomains = async (page: number = 1, filters: FilterSearch) => {
    setLoading(true);
    const response = await getData(page, filters);

    setDomains(response);
    setLoading(false);
  };

  const searchDomains = async (
    search: string,
    page: number = 1,
    filter: FilterSearch
  ) => {
    setLoading(true);
    const response = await searchData(search, page, filter);

    setDomains(response);
    setLoading(false);
  };

  React.useEffect(() => {
    if (searchTerm) {
      searchDomains(searchTerm, page, filter);
    } else {
      getDomains(page, filter);
    }
  }, [page, filter]); //eslint-disable-line

  React.useEffect(() => {
    if (searchTerm) {
      searchDomains(searchTerm, page, filter);
    } else {
      setPage(1);
      getDomains(page, filter);
    }
  }, [debounceValue]); // eslint-disable-line

  React.useEffect(() => {
    if (searchTerm === "") {
      router.replace("/");
    }
  }, [searchTerm]); // eslint-disable-line

  return (
    <DomainContext.Provider
      value={{
        getDomains,
        searchDomains,
        domains,
        setLoading,
        isLoading,
        setPage,
        page,
        setSearchTerm,
        searchTerm,
        setFilter,
        filter,
      }}
    >
      {children}
    </DomainContext.Provider>
  );
};

export default DomainProvider;
