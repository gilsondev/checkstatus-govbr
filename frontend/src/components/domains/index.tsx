"use client";

import Skeleton from "@/app/skeleton";
import Card from "../card";
import React from "react";
import { DomainContext, DomainContextType } from "@/app/context";
import { DomainsResponse } from "@/utils/types";
import clsx from "clsx";

const Domains = () => {
  const [page, setPage] = React.useState<number>(1);

  const { getDomains, domains, isLoading } =
    React.useContext<DomainContextType>(DomainContext);

  if (isLoading) {
    return <Skeleton />;
  }

  if (!isLoading && domains.items.length === 0) {
    return (
      <div>
        <h2 className="p-4 md:p-14 text-xl md:text-2xl lg:text-3xl text-gray-700 text-center">
          Nenhum domínio encontrado
        </h2>
      </div>
    );
  }

  return (
    !isLoading && (
      <main className="grid sm:grid-cols-2 md:grid-cols-1 gap-x-3" id="domains">
        <div className="px-5 pt-5 md:px-5 lg:px-16 flex flex-wrap justify-center gap-3">
          {domains?.items?.map((domain) => (
            <Card key={domain.slug} domain={domain} />
          ))}
        </div>

        <div className="flex justify-center py-5">
          <button
            disabled={domains.page === 1}
            onClick={() => getDomains(domains.page - 1)}
            // className="flex items-center justify-center px-4 h-10 text-base font-medium text-blue-950 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700"
            className={clsx(
              "flex items-center justify-center px-4 h-10 text-base font-medium",
              domains.page <= 1 && "opacity-30",
              "text-blue-950 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700"
            )}
          >
            Anterior
          </button>

          <button
            onClick={() => getDomains(domains.page + 1)}
            disabled={domains.page === domains.pages}
            className="flex items-center justify-center px-4 h-10 ml-3 text-base font-medium text-blue-950 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700"
          >
            Próximo
          </button>
        </div>
      </main>
    )
  );
};

export default Domains;
