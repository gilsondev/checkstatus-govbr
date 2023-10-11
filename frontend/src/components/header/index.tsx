import React from "react";

import InputSearch from "../inputsearch";

const Header = () => {
  return (
    <header className="flex flex-col items-center bg-white border border-gray-300 rounded-md p-5 mt-5 md:mt-20">
      <h1 className="text-2xl md:text-3xl lg:text-4xl font-bold text-blue-950 text-center">
        Acompanhe todos os domínios públicos registrados
      </h1>
      <p className="hidden md:block font-extralight text-blue-950 pt-3 w-2/3 md:w-3/4 text-center lg:text-xl">
        Tenha acesso atualizado aos dados abertos de todos os endereços .gov.br
        registrados para acesso a sites e plataformas do governo
      </p>
      <InputSearch />
    </header>
  );
};

export default Header;
