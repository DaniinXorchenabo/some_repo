import React from "react";
import { getCurrentTheme } from "./utils";

function BeautifulInput(props) {
  const style = getCurrentTheme("/all");
  return (
    <input style={style.input} type={props.type} placeholder={props.text} />
  );
}
export default BeautifulInput;
