import { NextPage } from "next";
import React from "react";
//import { getCurrentTheme } from "./utils";
import MainTop from "./MainTop";
import MainLeft from "./MainLeft";
import MainRight from "./MainRight";
import Charts from "./Charts";
import Footer from "./Footer";

const PageContentsForIndex: NextPage = () => {
  //const style = getCurrentTheme();
  return (
    <>
      <MainTop />
      <div style={{ display: "inline-flex", textAlign: "center" }}>
        <MainLeft />
        <MainRight />
      </div>
      <Charts />
      <br />
      <Footer noFixed={true} />
    </>
  );
};

export default PageContentsForIndex;
