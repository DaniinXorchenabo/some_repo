import Head from "next/head";
import React from "react";

import LoginPageContent from "../ui/LoginPage";

const LoginPage = () => {
  return (
    <>
      <Head>
        <title>Hackoton</title>
      </Head>
      <LoginPageContent />
    </>
  );
};

export default LoginPage;
