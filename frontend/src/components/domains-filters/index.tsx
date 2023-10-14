import React from "react";
import Dropdown from "../dropdown";
import { DomainContext, DomainContextType } from "@/app/context";

const statusOptions = [
  { value: "active", label: "Ativos" },
  { value: "canceled", label: "Cancelados" },
];

const availabilityOptions = [
  { value: "true", label: "Disponível" },
  { value: "false", label: "Indisponível" },
];

const DomainsFilters = () => {
  const { domains, isLoading, filter, setFilter } =
    React.useContext<DomainContextType>(DomainContext);

  return (
    !isLoading && (
      <div className="flex flex-col md:flex-row justify-between items-center gap-4 mt-10 md:mx-3 p-2 md:p-5 bg-neutral-100 border border-zinc-200 rounded-md">
        <span className="flex-1 text-md md:text-base text-blue-950 font-semibold">
          Total de domínios: {domains.total}
        </span>
        <div className="flex-1 flex items-center w-full gap-2 md:gap-4">
          <Dropdown
            emptyOption="Por status"
            options={statusOptions}
            onChange={(e) => setFilter({ ...filter, status: e.target.value })}
            value={filter.status}
          />
          <Dropdown
            emptyOption="Por disponibilidade"
            options={availabilityOptions}
            onChange={(e) =>
              setFilter({ ...filter, available: e.target.value })
            }
            value={filter.available}
          />
        </div>
        <div>
          {(filter.available || filter.status) && (
            <button
              type="button"
              aria-label="Limpar filtros"
              onClick={(e) => setFilter({ available: "", status: "" })}
              className="w-40 h-8 text-white bg-blue-950 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm"
            >
              Limpar
            </button>
          )}
        </div>
      </div>
    )
  );
};

export default DomainsFilters;
