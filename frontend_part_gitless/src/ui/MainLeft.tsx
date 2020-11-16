import React from "react";
import { getCurrentTheme } from "./utils";

function MainLeft() {
  const style = getCurrentTheme("main/top");
  const large = { fontSize: "40px" };
  return (
    <div>
      <p style={large}>Найдите крутую работу, </p>
      <p style={large}>
        Использую <span style={style.statistics}>статистику</span>
      </p>
      <p>
        Используя данные по разным критерием мы расскажем какая работа будет
      </p>
      <p>актуальна в следующем году.</p>
      <button style={style.moreDetailsButton}>Подробнее</button>
    </div>
  );
}
export default MainLeft;
