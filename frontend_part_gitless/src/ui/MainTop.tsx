import React from "react";
import Link from "next/link";

import { getCurrentTheme } from "./utils";
const purpleColor = "#6C63FF";
let active = {
  color: "white",
  backgroundColor: purpleColor,
  borderRadius: "5%",
  borderColor: purpleColor,
  width: "245px", //150px
  height: "50px",
  marginLeft: "10px",
};
let passive = {
  color: "black",
  backgroundColor: "white",
  borderRadius: "5%",
  borderColor: purpleColor,
  width: "245px", //150px
  height: "50px",
  marginLeft: "10px",
};
function ActiveButton(props) {
  return <button style={active}>{props.text}</button>;
}
function PassiveButton(props) {
  return <button style={passive}>{props.text}</button>;
}

function MainTop() {
  //<PassiveButton text="Регистрация" />
  const style = getCurrentTheme("loginPage");
  return (
    <>
      <div style={style.loginTop}>
        <div>
          <p style={{ padding: "0 300px" }}>Ситуационные центры</p>
        </div>
        <div style={{ width: "40%" }}>&nbsp;</div>
        <div style={{ display: "inline-flex", marginRight: "10%" }}>
          <Link href="/reg">
            <div>
              <PassiveButton text="Регистрация" />
            </div>
          </Link>
          <Link href="/login">
            <div>
              <ActiveButton text="Войти" />
            </div>
          </Link>
        </div>
      </div>
    </>
  );
}
export default MainTop;
