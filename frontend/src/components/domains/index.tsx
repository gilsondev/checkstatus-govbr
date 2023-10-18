"use client";

import { useSearchParams } from "next/navigation";
import Skeleton from "@/components/skeleton";
import Card from "../card";
import React, { useEffect } from "react";
import { DomainContext, DomainContextType } from "@/app/context";
import Pagination from "../pagination";

const Domains = () => {
  const params = useSearchParams();
  const actualPageNumber = params.get("page") || 1;
  const search = params.get("search") || "";
  const { domains, isLoading, setPage, setSearchTerm } =
    React.useContext<DomainContextType>(DomainContext);

  useEffect(() => {
    setPage(Number(actualPageNumber));
  }, [actualPageNumber]); // eslint-disable-line

  useEffect(() => {
    if (search) {
      setPage(Number(actualPageNumber));
      setSearchTerm(search);
    }
  }, [search, actualPageNumber]); // eslint-disable-line

  if (isLoading) {
    return <Skeleton />;
  }

  if (!isLoading && domains.items?.length === 0) {
    return (
      <div>
        <h2 className="p-4 md:p-14 text-xl md:text-2xl lg:text-3xl text-gray-700 text-center">
          Nenhum domínio encontrado
        </h2>
      </div>
    );
  }

  return (
    <>
      {!isLoading && (
        <main className="grid grid-cols-1 gap-x-3 mt-10 mx-auto" id="domains">
          <div className="lg:my-2 lg:px-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-4 gap-3">
            {domains?.items?.map((domain) => (
              <Card key={domain.slug} domain={domain} />
            ))}
          </div>
          <div className="flex justify-center px-2 md:px-0 py-5">
            <Pagination page={domains.page} totalPages={domains.pages} />
          </div>
        </main>
      )}
    </>
  );
};

export default Domains;
