import "./globals.css";
import type { Metadata } from "next";
import { Montserrat } from "next/font/google";

const montserrat = Montserrat({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Checkstatus gov.br",
  description: `Tenha acesso atualizado aos dados abertos de todos os
  endereços .gov.br registrados para acesso a sites e plataformas do governo`,
  metadataBase: new URL("https://checkstatus.gov.br"),
  openGraph: {
    type: "website",
    title: "Checkstatus gov.br",
    siteName: "Checkstatus gov.br",
    description: `Tenha acesso atualizado aos dados abertos de todos os
    endereços .gov.br registrados para acesso a sites e plataformas do governo`,
    images: [
      {
        url: "./logo.png",
        width: 800,
        height: 600,
        type: "image/png",
      },
      {
        url: "./logo.png",
        width: 1800,
        height: 1600,
        type: "image/png",
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
        {children}
      </body>
    </html>
  );
}
