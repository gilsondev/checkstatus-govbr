import GAnalytics from "@/components/ganalytics";
import * as Sentry from "@sentry/nextjs";
import "./globals.css";
import type { Metadata } from "next";
import { Open_Sans } from "next/font/google";

Sentry.setTag("app", "Checkstatus Frontend");
const font = Open_Sans({
  subsets: ["latin"],
  weight: ["300", "400", "500", "700"],
});

export const metadata: Metadata = {
  title: "Checkstatus gov.br",
  description:
    "Tenha acesso atualizado aos dados abertos de todos os endereços .gov.br registrados para acesso a sites e plataformas do governo",
  metadataBase: new URL("https://checkstatus.gilsondev.in"),
  keywords: [
    "domínios públicos",
    "plataformas do governo",
    "sites do governo",
    "checkstatus",
    "checkstatus gov br",
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
      "Acompanhe os domínios públicos registrados e acesse dados abertos de endereços .gov.br.",
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

interface RootLayoutProps {
  children: React.ReactNode;
}

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="pt-BR">
      <body
        className={`${font.className} bg-zinc-50 grid grid-cols-1 items-center px-2 sm:px-5 md:px-16 pt-8`}
      >
        <GAnalytics />
        {children}
      </body>
    </html>
  );
}
