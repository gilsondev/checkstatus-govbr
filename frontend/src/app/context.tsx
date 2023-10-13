import React, { createContext } from "react";
import { DomainsResponse } from "../utils/types";
import { getData, searchData } from "../utils";
import { useDebounce } from "usehooks-ts";
import { useRouter } from "next/navigation";

export type DomainContextType = {
  getDomains: (page: number) => void;
  searchDomains: (search: string, page: number) => void;
  setLoading: (isLoading: boolean) => void;
  setPage: (page: number) => void;
  setSearchTerm: (searchTerm: string) => void;
  searchTerm: string;
  page: number;
  isLoading: boolean;
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
  page: 1,
  searchTerm: "",
  isLoading: true,
  domains: defaultDomainsValue,
});

const DomainProvider = ({ children }: { children: React.ReactNode }) => {
  const router = useRouter();

  const [isLoading, setLoading] = React.useState(true);
  const [page, setPage] = React.useState<number>(1);
  const [searchTerm, setSearchTerm] = React.useState<string>("");
  const [domains, setDomains] =
    React.useState<DomainsResponse>(defaultDomainsValue);

  const debounceValue = useDebounce<string>(searchTerm, 500);

  const getDomains = async (page: number = 1) => {
    setLoading(true);
    const response = await getData(page);

    setDomains(response);
    setLoading(false);
  };

  const searchDomains = async (search: string, page: number = 1) => {
    setLoading(true);
    const response = await searchData(search, page);

    setDomains(response);
    setLoading(false);
  };

  React.useEffect(() => {
    if (searchTerm) {
      searchDomains(searchTerm, page);
    } else {
      getDomains(page);
    }
  }, [page]); //eslint-disable-line

  React.useEffect(() => {
    if (searchTerm) {
      searchDomains(searchTerm, page);
    } else {
      setPage(1);
      getDomains(page);
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
      }}
    >
      {children}
    </DomainContext.Provider>
  );
};

export default DomainProvider;
