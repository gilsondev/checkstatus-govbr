"use client";

import Header from "@/components/header";
import Domains from "@/components/domains";
import DomainProvider from "./context";

import React from "react";
import Navbar from "@/components/navbar";
import DomainsFilters from "@/components/domains-filters";

export default function Home() {
  return (
    <DomainProvider>
      <Navbar />
      <Header />
      <DomainsFilters />
      <Domains />
    </DomainProvider>
  );
}
