"use client";

import { DomainContext } from "@/app/context";
import React from "react";
import { useDebounce } from "usehooks-ts";

const InputSearch = () => {
  const { searchDomains } = React.useContext(DomainContext);
  const [searchTerm, setSearchTerm] = React.useState("");
  const debounceValue = useDebounce<string>(searchTerm, 500);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { value } = event.target;
    setSearchTerm(value);
  };

  React.useEffect(() => {
    if (searchTerm) {
      searchDomains(searchTerm);
    }
  }, [debounceValue]); // eslint-disable-line

  return (
    <div className="mt-10 w-full lg:w-1/2 text-center">
      <form>
        <label className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">
          Pesquisar
        </label>
        <div className="relative">
          <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg
              className="w-4 h-4 text-gray-500 dark:text-gray-400"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 20"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
              />
            </svg>
          </div>
          <input
            type="search"
            name="search"
            onChange={handleChange}
            id="default-search"
            className="block w-full p-4 pl-10 text-sm md:text-md text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500"
            placeholder="Busque domínio ou organização"
            required
          />
        </div>
      </form>
    </div>
  );
};

export default InputSearch;
