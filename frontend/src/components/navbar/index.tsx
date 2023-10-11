import Image from "next/image";
import Link from "next/link";
import React from "react";
import { BsGithub } from "react-icons/bs";

const Navbar = () => {
  return (
    <nav className="md:flex gap-2 md:gap-5 lg:gap-10 justify-between items-center">
      <Link href="/" className="flex justify-center md:block">
        <Image
          src="/logo.svg"
          width={250}
          height={50}
          alt="Checkstatus gov.br"
        />
      </Link>
      <ul className="hidden md:flex gap-2 md:gap-6 mt-1">
        <li>
          <Link
            href="https://github.com/gilsondev/checkstatus-govbr"
            target="_blank"
          >
            <BsGithub size={24} className="text-blue-950 hover:text-blue-700" />
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
