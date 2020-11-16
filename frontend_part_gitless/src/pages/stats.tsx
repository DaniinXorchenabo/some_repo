import Head from "next/head";
import React from "react";

import StatsPageContent from "../ui/StatsPage";

const StatsPage = () => {
  return (
    <>
      <Head>
        <title>Hackoton</title>
      </Head>
      <StatsPageContent />
    </>
  );
};

export default StatsPage;
