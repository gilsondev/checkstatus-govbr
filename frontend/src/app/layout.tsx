import GAnalytics from "@/components/ganalytics";
import * as Sentry from "@sentry/nextjs";
import "./globals.css";
import type { Metadata } from "next";
import { Montserrat } from "next/font/google";

Sentry.setTag("app", "Checkstatus Frontend");

const montserrat = Montserrat({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Checkstatus gov.br",
  description:
    "Tenha acesso atualizado aos dados abertos de todos os endereços .gov.br registrados para acesso a sites e plataformas do governo",
  metadataBase: new URL("https://checkstatus.gilsondev.in"),
  keywords: [
    "checkstatus",
    "dominios govbr",
    "enderecos do governo federal",
    "dados abertos",
    "dados abertos do governo",
    "dados abertos dos dominios",
    "enderecos .gov.br",
  ],
  openGraph: {
    type: "website",
    title: "Checkstatus gov.br",
    siteName: "Checkstatus gov.br",
    description:
      "Tenha acesso atualizado aos dados abertos de todos os endereços .gov.br registrados para acesso a sites e plataformas do governo",
    url: "https://checkstatus.gilsondev.in",
    images: [
      {
        url: "./opengraph_image.svg",
        width: 800,
        height: 600,
        type: "image/svg",
      },
      {
        url: "./opengraph_image.svg",
        width: 1800,
        height: 1600,
        type: "image/svg",
      },
    ],
    locale: "pt_BR",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body
        className={`${montserrat.className} bg-gray-200 grid grid-cols-1 items-center px-5 md:px-16 pt-8`}
      >
        <GAnalytics />
        {children}
      </body>
    </html>
  );
}
