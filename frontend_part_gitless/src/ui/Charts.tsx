import React from "react";
import { getCurrentTheme } from "./utils";

type ChartData = { header: string; key: number };

function Chart(props: ChartData) {
  const style = getCurrentTheme("main/charts");
  return (
    <div style={style.chart}>
      <div style={{ display: "inline-flex" }}>
        <p style={style.chartHeader}>{props.header}&nbsp;</p>
        <p style={style.moreDetails}>Подробнее&gt;&gt;</p>
      </div>
      <img src="chart.png" />
    </div>
  );
}

function Charts() {
  //const style = getCurrentTheme("main/charts");
  const topHeaders = ["Образование", "Заработок", "Возраст"];
  let topCharts = topHeaders.map((v, i) => {
    return <Chart header={v} key={i} />;
  });
  const bottomHeaders = ["Пол", "График", "Квалифицикация"];
  let bottomCharts = bottomHeaders.map((v, i) => {
    return <Chart header={v} key={i} />;
  });
  return (
    <>
      <p style={{ textAlign: "center", fontWeight: 500, fontSize: "30px" }}>
        Виды графиков
      </p>
      <div style={{ display: "block" }}>
        <div style={{ display: "inline-flex", width: "120%" }}>{topCharts}</div>
        <div style={{ height: "10%" }}>&nbsp;</div>
        <div style={{ display: "inline-flex", width: "120%" }}>
          {bottomCharts}
        </div>
      </div>
    </>
  );
}
export default Charts;
