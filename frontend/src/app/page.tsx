"use client";

import Header from "@/components/header";
import Domains from "@/components/domains";
import { DomainsResponse } from "@/types";

import React from "react";

export default function Home() {
  return (
    <>
      <Header />
      <Domains />
    </>
  );
}
