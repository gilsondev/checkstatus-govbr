"use client";

import Header from "@/components/header";
import Domains from "@/components/domains";
import DomainProvider from "./context";

import React from "react";

export default function Home() {
  return (
    <DomainProvider>
      <Header />
      <Domains />
    </DomainProvider>
  );
}
