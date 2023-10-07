"use client";

import Header from "@/components/header";
import Domains from "@/components/domains";
import { DomainsResponse } from "@/types";

import React, { Suspense } from "react";
import Skeleton from "./skeleton";

interface HomeProps {
  searchParams: {
    [key: string]: string | string[] | undefined;
  };
}

export default function Home({ searchParams }: HomeProps) {
  const [domains, setDomains] = React.useState<DomainsResponse>({
    items: [],
    total: 0,
    page: Number(process.env.NEXT_PUBLIC_PAGINATION_INITIAL_PAGE),
    size: Number(process.env.NEXT_PUBLIC_PAGINATION_SIZE),
    pages: 0,
  });

  React.useEffect(() => {
    const page = searchParams.page
      ? Number(searchParams.page)
      : Number(process.env.NEXT_PUBLIC_PAGINATION_INITIAL_PAGE);

    const fetchData = async () => {
      const data = await getData(page);
      setDomains(data);
    };
    fetchData();
  }, [searchParams]);

  return (
    <>
      <Header />
      <Suspense fallback={<Skeleton />}>
        <Domains {...domains} />
      </Suspense>
    </>
  );
}

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
