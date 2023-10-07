import Header from "@/components/header";
import Domains from "@/components/domains";
import { DomainsResponse } from "@/types";

import { Suspense } from "react";
import Skeleton from "./skeleton";

interface HomeProps {
  searchParams: {
    [key: string]: string | string[] | undefined;
  };
}

export default async function Home({ searchParams }: HomeProps) {
  const page =
    Number(searchParams.page) || Number(process.env.PAGINATION_INITIAL_PAGE);
  const domains = await getData(page);

  return (
    <>
      <Header />
      <Suspense fallback={<Skeleton />}>
        <Domains {...domains} />
      </Suspense>
    </>
  );
}

async function getData(
  page: number,
  size: number = Number(process.env.PAGINATION_SIZE)
): Promise<DomainsResponse> {
  const res = await fetch(
    `${process.env.CHECKSTATUS_API_URL}/domains?page=${page}&size=${size}`,
    {
      cache: "no-store",
    }
  );

  return res.json();
}
