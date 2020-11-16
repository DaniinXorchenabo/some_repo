import React from "react";
import { getCurrentTheme } from "./utils";

function LoginTop() {
  const style = getCurrentTheme("loginPage");
  return (
    <>
      <div style={style.loginTop}>
        <div>
          <p style={{ padding: "0 300px" }}>Ситуационные центры</p>
        </div>
        <div style={{ width: "40%" }}>&nbsp;</div>
      </div>
    </>
  );
}
export default LoginTop;
