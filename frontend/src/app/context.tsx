import React, { createContext } from "react";
import { DomainsResponse } from "../utils/types";
import { getData } from "../utils";

export type DomainContextType = {
  getDomains: (page: number) => void;
  searchDomains: (search: string) => void;
  setLoading: (isLoading: boolean) => void;
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
  isLoading: true,
  domains: defaultDomainsValue,
});

const DomainProvider = ({ children }: { children: React.ReactNode }) => {
  const [isLoading, setLoading] = React.useState(true);
  const [domains, setDomains] =
    React.useState<DomainsResponse>(defaultDomainsValue);

  const getDomains = async (page: number = 1) => {
    setLoading(true);
    const response = await getData(page);

    setDomains(response);
    setLoading(false);
  };

  const searchDomains = async (search: string) => {
    setLoading(true);
    const response = await getData(1, search);

    setDomains(response);
    setLoading(false);
  };

  React.useEffect(() => {
    getDomains();
  }, []);

  return (
    <DomainContext.Provider
      value={{ getDomains, searchDomains, domains, setLoading, isLoading }}
    >
      {children}
    </DomainContext.Provider>
  );
};

export default DomainProvider;
