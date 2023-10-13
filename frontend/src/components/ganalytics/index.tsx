import Script from "next/script";
import React from "react";

export const GA_MEASUREMENT_ID = process.env.NEXT_PUBLIC_GOOGLE_ID;

const GAnalytics = () => {
  return (
    <div>
      <Script src="https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}" />
      <Script id="google-analytics">
        {`
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', '${GA_MEASUREMENT_ID}');
        `}
      </Script>
    </div>
  );
};

export default GAnalytics;
