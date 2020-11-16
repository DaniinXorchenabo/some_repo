import { CSSProperties } from "react";

const purpleColor = "#6C63FF";

const a: CSSProperties = {
  color: purpleColor,
  textDecoration: "underline",
};
const chart: CSSProperties = {
  backgroundColor: "white",
  color: "black",
  width: "20%",
  padding: "0 50px", //TODO: new
};
const chartHeader: CSSProperties = {
  fontWeight: 600,
};
const moreDetails: CSSProperties = {
  fontWeight: "normal",
  color: purpleColor,
};
const variantsOfCharts: CSSProperties = {
  color: "#080723",
};
const moreDetailsButton: CSSProperties = {
  color: "white",
  backgroundColor: purpleColor,
  borderRadius: "5%",
  borderColor: purpleColor,
  width: "150px",
  height: "50px",
};
const statistics: CSSProperties = {
  color: purpleColor,
};
//footer
const footer: CSSProperties = {
  position: "fixed",
  width: "100%",
  display: "inline-flex",
  background: "#2F2E41",
  bottom: "0",
  color: "white",
};
const footerNoFixed: CSSProperties = {
  width: "100%",
  display: "inline-flex",
  background: "#2F2E41",
  bottom: "0",
  color: "white",
};
const button: CSSProperties = {
  color: "white",
  backgroundColor: purpleColor,
  borderRadius: "5%",
  borderColor: purpleColor,
  width: "50%", //150px
  height: "50px",
  marginLeft: "10px",
};
const input: CSSProperties = {
  width: "50%",
  height: "50px",
  border: "1px solid #DADADA",
  boxSizing: "border-box",
  borderRadius: "5px",
  marginTop: "20px",
};
const loginTop: CSSProperties = {
  //marginLeft: "20%",
  display: "flex",
  background: "white",
};
const loginMain: CSSProperties = {
  width: "25%",
  marginLeft: "40%",
  textAlign: "center",
  background: "white",
  border: "2px solid #CECBFF",
  borderRadius: "16px",
};
const analitic: CSSProperties = {
  color: purpleColor,
};
const selectParams: CSSProperties = {
  marginLeft: "30%",
  marginRight: "30%",
  color: "white",
  background: purpleColor,
  borderRadius: "8px",
};
const dark = {
  top: { statistics, moreDetailsButton },
  charts: { chart, chartHeader, moreDetails },
  footer: { footer, footerNoFixed },
  all: { input, button },
  loginPage: { loginTop, a, loginMain }, //and reg page too
  stats: { analitic, selectParams },
};
export default dark;
