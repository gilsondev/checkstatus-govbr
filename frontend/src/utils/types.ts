export type Domain = {
  created_at: string;
  updated_at: string;
  domain: string;
  slug: string;
  document: string;
  organization: string;
  agent: string;
  registered_at: string;
  refreshed_at: string;
  available: boolean;
};

export type DomainsResponse = {
  items: Domain[];
  total: number;
  page: number;
  size: number;
  pages: number;
};
