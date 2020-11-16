import React from "react";
import { getCurrentTheme } from "./utils";

function StatsTop() {
  const style = getCurrentTheme("stats");
  const analitic = "Здравствуйте, <pre style={style.analitic}>Аналитик</pre>";
  //Здравствуйте, {analitic}
  return (
    <>
      <div style={style.loginTop}>
        <div style={{ display: "inline-flex" }}>
          <pre style={{ padding: "0 300px" }}>Ситуационные центры</pre>
          <pre
            style={{ padding: "0 300px" }}
            dangerouslySetInnerHTML={{ __html: analitic }}
          ></pre>
        </div>
        <div style={{ width: "40%" }}>&nbsp;</div>
      </div>
    </>
  );
}
export default StatsTop;
