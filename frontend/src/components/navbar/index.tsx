import React from "react";

const Navbar = () => {
  return (
    <nav className="md:flex gap-2 md:gap-5 lg:gap-10 items-center">
      <h1 className="text-center text-xl md:block md:text-2xl lg:text-3xl font-medium text-blue-950">
        Checkstatus gov.br
      </h1>
      <ul className="hidden md:flex gap-2 md:gap-6 mt-1 font-medium md:text-lg">
        <li>
          <a href="/" className="hover:text-blue-900">
            Home
          </a>
        </li>
        <li>
          <a href="/" className="hover:text-blue-900">
            Sobre
          </a>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
