import "../ui/index.css";
import "../ui/PageContentsForIndex.css";

import { AppProps } from "next/app";
import Head from "next/head";
import React, { useEffect } from "react";

const App: React.FunctionComponent<AppProps> = ({ Component, pageProps }) => {
  /*useEffect(() => {
    let pageHeight = document.documentElement.scrollHeight;
    let obj = document.body;
    if (obj.style.height > pageHeight) {
      document.querySelector("#footer").style.position = "absolute";
    }
  }); */
  return (
    <>
      <Head>
        <link rel="apple-touch-icon" href="/logo192.png" />
        <link rel="icon" href="/favicon.ico" />
        <link rel="manifest" href="/manifest.json" />
        <meta name="theme-color" content="#000000" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <Component {...pageProps} />
    </>
  );
};

export default App;
