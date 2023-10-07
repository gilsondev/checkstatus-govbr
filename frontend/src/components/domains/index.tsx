import Card from "../card";
import { Domain } from "@/types";
import Link from "next/link";

interface DomainsProps {
  items: Domain[];
  total: number;
  page: number;
  pages: number;
}

const Domains = ({ items, page, pages }: DomainsProps) => {
  return (
    <main className="grid sm:grid-cols-2 md:grid-cols-1 gap-x-3" id="domains">
      <div className="px-5 md:px-5 lg:px-16 flex flex-wrap justify-center gap-3">
        {items?.map((domain) => (
          <Card key={domain.slug} domain={domain} />
        ))}
      </div>

      <div className="flex justify-center mb-5">
        {page > 1 && (
          <Link
            href={{
              pathname: "/",
              query: {
                page: page > 1 ? page - 1 : 1,
              },
            }}
            className="flex items-center justify-center px-4 h-10 text-base font-medium text-blue-950 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700"
          >
            Anterior
          </Link>
        )}

        {page < pages && (
          <Link
            href={{
              pathname: "/",
              query: {
                page: page + 1,
              },
            }}
            className="flex items-center justify-center px-4 h-10 ml-3 text-base font-medium text-blue-950 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700"
          >
            Próximo
          </Link>
        )}
      </div>
    </main>
  );
};

export default Domains;
