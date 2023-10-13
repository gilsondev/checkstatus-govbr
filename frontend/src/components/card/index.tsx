import { Domain } from "@/utils/types";
import Image from "next/image";
import Link from "next/link";
import React from "react";

interface CardProps {
  domain: Domain;
}

const Card = ({ domain }: CardProps) => {
  const isActive = domain.status.includes("active");
  const isAvailable = domain.available;
  const availabilityDetails = [
    {
      condition: isAvailable && isActive,
      className: "bg-green-100 text-green-800",
      text: "Site Disponível",
    },
    {
      condition: !isAvailable && isActive,
      className: "bg-yellow-100 text-yellow-800",
      text: "Site Indisponível",
    },
  ];

  const domainStatusDetails = [
    {
      condition: isActive,
      className: "bg-green-100 text-green-800",
      text: "Domínio Ativo",
    },
    {
      condition: !isActive,
      className: "bg-red-100 text-red-800",
      text: "Domínio Cancelado",
    },
  ];

  const homapageImage = (domain: Domain) => {
    const domainFilename = domain.domain.replace(/\./g, "_");
    const homepageImagesCDN = process.env.NEXT_PUBLIC_HOMEPAGE_IMAGES_CDN;

    return `${homepageImagesCDN}/homepages/10_2023/${domainFilename}.jpg`;
  };

  return (
    <div className="px-2 lg:my-4 lg:px-4 p-6 max-w-sm bg-neutral-100 border border-zync-300 rounded-md hover:bg-zync-100">
      <div className="mb-5 bg-neutral-50 rounded-md">
        <Image
          src={homapageImage(domain)}
          alt={domain.domain}
          width={350}
          height={197}
          className="rounded-md w[350px] h-[197px]"
          style={{ objectFit: "contain" }}
        />
      </div>
      {isActive && (
        <Link href={`http://${domain.domain}`} target="_blank">
          <h3 className="mb-2 text-xl w-full md:text-2xl font-bold break-words tracking-tight text-blue-950 hover:text-blue-500">
            {domain.domain}
          </h3>
        </Link>
      )}
      {!isActive && (
        <h3 className="mb-2 text-xl w-full md:text-2xl font-bold tracking-tight text-gray-500 ">
          {domain.domain}
        </h3>
      )}
      <div>
        {availabilityDetails.map((detail, index) =>
          detail.condition ? (
            <span
              key={index}
              className={`text-xs font-medium mr-2 px-2.5 py-0.5 rounded ${detail.className}`}
            >
              {detail.text}
            </span>
          ) : null
        )}
        {domainStatusDetails.map((detail, index) =>
          detail.condition ? (
            <span
              key={index}
              className={`text-xs font-medium mr-2 px-2.5 py-0.5 rounded ${detail.className}`}
            >
              {detail.text}
            </span>
          ) : null
        )}
      </div>
      <div className="flex flex-col gap-2 mt-4">
        <span className="text-sm text-gray-500 break-words">
          <strong>Organização: </strong>
          {domain.organization}
        </span>
        <span className="text-sm text-gray-500">
          <strong>CNPJ: </strong>
          {domain.document}
        </span>
        <span className="text-sm text-gray-500 break-words">
          <strong>Responsável: </strong>
          {domain.agent}
        </span>
        <span className="text-sm text-gray-500">
          <strong>Registrado: </strong>{" "}
          {new Date(domain.registered_at).toLocaleDateString("pt-BR")}
        </span>
        <span className="text-sm text-gray-500">
          <strong>Última renovação: </strong>{" "}
          {new Date(domain.refreshed_at).toLocaleDateString("pt-BR")}
        </span>
      </div>
    </div>
  );
};

export default Card;
