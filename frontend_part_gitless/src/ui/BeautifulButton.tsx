import React from "react";
import { getCurrentTheme } from "./utils";
function BeautifulButton(props) {
  const style = getCurrentTheme("all");
  //if (props.background !== undefined) style.button.background = props.background;
  return <button style={style.button}>{props.text}</button>;
}
export default BeautifulButton;
