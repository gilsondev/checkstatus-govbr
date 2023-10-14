import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const page =
    Number(searchParams.get("page")) || process.env.PAGINATION_INITIAL_PAGE;
  const size = process.env.PAGINATION_SIZE;
  const search = searchParams.get("search");
  const available = searchParams.get("available");
  const status = searchParams.get("status");

  let baseUrl = `${process.env.CHECKSTATUS_API_URL}/domains?page=${page}&size=${size}`;
  if (search) {
    baseUrl += `&search=${search}`;
  }
  if (available) {
    baseUrl += `&available=${available}`;
  }
  if (status) {
    baseUrl += `&status=${status}`;
  }

  const response = await fetch(baseUrl, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const data = await response.json();

  return Response.json(data);
}
