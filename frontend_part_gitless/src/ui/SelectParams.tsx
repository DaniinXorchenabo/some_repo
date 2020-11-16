import React, { useEffect, useState } from "react";
import { getCurrentTheme } from "./utils";

const purpleColor = "red";
let button = {
  color: "white",
  backgroundColor: purpleColor,
  borderRadius: "5%",
  borderColor: purpleColor,
  width: "245px", //150px
  height: "50px",
  marginLeft: "25%",
};
function Label(props) {
  return (
    <div>
      <p
        onClick={() => {
          props.rl(props.text);
        }}
      >
        {props.text} <img src="close.png" />
      </p>
    </div>
  );
}
function Param(props) {
  const style = getCurrentTheme("stats"); //all???
  const [labels, setLabels] = useState([] as any);
  const options = {
    Сфера: ["С/х", "IT"],
    Квалификация: ["Учащийся", "Высшее образование"],
    Вакансии: ["Вакансия 1", "Вакансия 2"],
  };
  const addLabel = (e) => {
    const text = e.target.value;
    if (labels.includes(text)) {
      console.warn("Validation Error");
      return;
    }
    const copy: any = labels.slice();
    copy.push(text); //it's okey
    setLabels(copy);
  };
  const removeLabel = (name) => {
    const copy: any = labels.slice();
    copy.splice(copy.indexOf(name), 1);
    setLabels(copy);
  };
  const removeAll = () => setLabels([]);
  return (
    <div>
      <div style={{ display: "inline-flex" }}>
        <p>{props.text}</p>
        <select onChange={addLabel} style={{ width: "200%" }}>
          {options[props.text].map((v, i) => {
            return <option>{v}</option>;
          })}
        </select>
      </div>
      <div style={{ display: "inline-flex", padding: "0 20px" }}>
        {labels.map((v, i) => {
          return <Label text={v} key={i} rl={removeLabel} />;
        })}
        <Label text="Delete All" rl={removeAll} />
      </div>
    </div>
  );
}
function AnotherParam(props) {
  const [firstYear, setFirstYear] = useState(2016);
  const [SecondYear, setSecondYear] = useState(2017);
  useEffect(() => {
    props.setter(`${firstYear}@${SecondYear}`);
  }, [firstYear, SecondYear]);
  let options: number[] = [];
  for (let i = 2016; i < 2020; i++) options.push(i);
  return (
    <div style={{ display: "inline-flex" }}>
      <p>Временной период</p>
      <select onChange={(e) => setFirstYear(+e.target.value)}>
        {options.map((v, i) => {
          return <option key={i}>{v} </option>;
        })}
      </select>
      <p>-</p>
      <select onChange={(e) => setSecondYear(+e.target.value)}>
        {options.slice(1).map((v, i) => {
          return <option key={i}>{v} </option>;
        })}
      </select>
    </div>
  );
}
function SelectParams() {
  ///test?field_of_activity=bool_or_name&qualification=bool_or_name&age=1@3@5-10&work_years=1@3@5-10&gender=m|w|mw
  const [field_of_activity, setFieldOfActivity] = useState("bool_or_true");
  const [qualification, setQualification] = useState("bool_or_true");
  const [age, setAge] = useState("1@3@5-10");
  const [work_years, setWorkYears] = useState("1");
  const [gender, setGender] = useState("m");
  const onError = (err) => {
    console.error(err);
    alert("Произошла ошибка. Обратитесь в техподдержку");
  };
  function stringify(object) {
    let str = "?";
    let keys = Object.keys(object);
    for (let i = 0; i < keys.length; i++)
      str += `${keys[i]}=${object[keys[i]]}&`;
    const tmp = str.slice(0, str.length - 1);
    return encodeURI(tmp);
  }
  useEffect(() => {
    const body = {
      field_of_activity,
      qualification,
      age,
      work_years,
      gender: "m|w|mw",
    };
    fetch(`https://weirdeproject.pythonanywhere.com/test${stringify(body)}`)
      .then((data) => data.json())
      .then((data) => console.log(data))
      .catch(onError);
  }, [field_of_activity, qualification, age, gender]);
  return (
    <div style={{ width: "100%" }}>
      <Param text="Сфера" setter={setFieldOfActivity} />
      <Param text="Квалификация" setter={setQualification} />
      <Param text="Вакансии" />
      <AnotherParam setter={setWorkYears} /> <br />
      <button style={button}>Отправить</button>
    </div>
  );
}
export default SelectParams;
