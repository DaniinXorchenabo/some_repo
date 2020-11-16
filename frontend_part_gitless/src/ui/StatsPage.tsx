import React, { useEffect } from "react";
import StatsTop from "./StatsTop";
import StatsMain from "./StatsMain";
import Footer from "./Footer";

function StatsPage() {
  return (
    <div>
      <StatsTop />
      <StatsMain />
      <Footer noFixed={true} />
    </div>
  );
}
export default StatsPage;
