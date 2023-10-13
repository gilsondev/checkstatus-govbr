import { DomainsResponse } from "@/utils/types";
import React from "react";

interface DomainsHeader {
  domains: DomainsResponse;
}

const DomainsHeader = ({ domains }: DomainsHeader) => {
  return (
    <div className="flex my-3 lg:mt-10 mx-0 lg:mx-4">
      <span className="text-base md:text-xl font-bold text-blue-950">
        Encontrado {domains.total} {domains.total > 1 ? "domínios" : "domínio"}
      </span>
    </div>
  );
};

export default DomainsHeader;
