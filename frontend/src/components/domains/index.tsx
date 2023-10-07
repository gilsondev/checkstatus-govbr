"use client";

import Skeleton from "@/app/skeleton";
import Card from "../card";
import { Domain, DomainsResponse } from "@/types";
import React from "react";

const Domains = () => {
  const [isLoading, setLoading] = React.useState(true);
  const [domains, setDomains] = React.useState<DomainsResponse>({
    items: [],
    total: 0,
    page: 0,
    size: 0,
    pages: 0,
  });
  const [page, setPage] = React.useState(
    Number(process.env.NEXT_PUBLIC_PAGINATION_INITIAL_PAGE)
  );

  React.useEffect(() => {
    const fetchData = async () => {
      setLoading(true);

      const data = await getData(page);
      setDomains(data);
      setLoading(false);
    };
    fetchData();
  }, [page]);

  if (isLoading) {
    return <Skeleton />;
  }

  return (
    !isLoading && (
      <main className="grid sm:grid-cols-2 md:grid-cols-1 gap-x-3" id="domains">
        <div className="px-5 md:px-5 lg:px-16 flex flex-wrap justify-center gap-3">
          {domains.items?.map((domain) => (
            <Card key={domain.slug} domain={domain} />
          ))}
        </div>

        <div className="flex justify-center mb-5">
          <button
            disabled={page === 1}
            onClick={() => setPage(page - 1)}
            className="flex items-center justify-center px-4 h-10 text-base font-medium text-blue-950 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700"
          >
            Anterior
          </button>

          <button
            onClick={() => setPage(page + 1)}
            disabled={page === domains.pages}
            className="flex items-center justify-center px-4 h-10 ml-3 text-base font-medium text-blue-950 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700"
          >
            Próximo
          </button>
        </div>
      </main>
    )
  );
};

const getData = async (
  page: number,
  size: number = Number(process.env.NEXT_PUBLIC_PAGINATION_SIZE)
): Promise<DomainsResponse> => {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_CHECKSTATUS_API_URL}/domains?page=${page}&size=${size}`,
    {
      cache: "no-store",
    }
  );

  return res.json();
};

export default Domains;
