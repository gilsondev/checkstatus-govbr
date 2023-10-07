"use client";

import { Domain } from "@/utils/types";
import React from "react";

interface CardProps {
  domain: Domain;
}

const Card = ({ domain }: CardProps) => {
  return (
    <a
      href={`http://${domain.domain}`}
      target="_blank"
      className="w-full lg:my-4 lg:px-4 max-w-sm p-6 bg-white border border-gray-200 rounded-md shadow hover:bg-gray-50"
    >
      <h5 className="mb-2 text-xl w-full md:text-2xl font-bold tracking-tight text-blue-950">
        {domain.domain}
      </h5>
      <div className="flex flex-col gap-2 mt-4">
        <span className="text-sm text-gray-500">
          <strong>Organização: </strong>
          {domain.organization}
        </span>
        <span className="text-sm text-gray-500">
          <strong>CNPJ: </strong>
          {domain.document}
        </span>
        <span className="text-sm text-gray-500">
          <strong>Responsável: </strong>
          {domain.agent}
        </span>
        <span className="text-sm text-gray-500">
          <strong>Registrado: </strong>{" "}
          {new Date(domain.registered_at).toLocaleDateString("pt-BR")}
        </span>
        <span className="text-sm text-gray-500">
          <strong>Última renovação: </strong>{" "}
          {new Date(domain.updated_at).toLocaleDateString("pt-BR")}
        </span>
      </div>
    </a>
  );
};

export default Card;
