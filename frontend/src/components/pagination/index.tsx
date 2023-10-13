import clsx from "clsx";
import Link from "next/link";
import React from "react";

interface PaginationProps {
  page: number;
  totalPages: number;
}

const Pagination = ({ page, totalPages }: PaginationProps) => {
  const numbers = (num: number, quantity: number) => {
    let numbers = [];
    const maxNumbers = quantity > 5 ? 5 : quantity;

    if (num <= quantity) {
      for (let i = 1; i <= maxNumbers; i++) {
        numbers.push(i);
      }
    } else {
      for (
        let i = num - Math.floor(maxNumbers / 2);
        i <= num + Math.ceil(maxNumbers / 2) - 1;
        i++
      ) {
        numbers.push(i);
      }
    }

    return numbers;
  };

  return (
    <nav aria-label="Paginação">
      <ul className="inline-flex -space-x-px text-base h-10">
        <li>
          {page === 1 ? (
            <span className="flex items-center cursor-pointer justify-center px-4 h-10 leading-tight font-semibold text-sm md:text-base text-gray-500 bg-white border border-gray-300 rounded-l-lg opacity-50">
              Anterior
            </span>
          ) : (
            <Link
              href={`?page=${page - 1}`}
              className="flex items-center justify-center px-4 h-10 ml-0 leading-tight font-semibold text-sm md:text-base text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700"
            >
              Anterior
            </Link>
          )}
        </li>
        {numbers(page, totalPages).map((number) => (
          <li key={number}>
            <Link
              href={`?page=${number}`}
              className={clsx(
                "flex items-center justify-center px-3 md:px-4 h-10 leading-tight text-sm md:text-base text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700",
                page === number && "bg-zinc-200 text-gray-700"
              )}
            >
              {number}
            </Link>
          </li>
        ))}
        <li>
          {page === totalPages ? (
            <span className="flex items-center cursor-pointer justify-center px-4 h-10 leading-tight text-sm md:text-base font-semibold text-gray-500 bg-white border border-gray-300 rounded-r-lg opacity-50">
              Próximo
            </span>
          ) : (
            <Link
              href={`?page=${page + 1}`}
              className="flex items-center justify-center px-4 h-10 leading-tight font-semibold text-sm md:text-base text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700"
            >
              Próximo
            </Link>
          )}
        </li>
      </ul>
    </nav>
  );
};

export default Pagination;
