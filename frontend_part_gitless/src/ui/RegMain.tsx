import React from "react";
import { getCurrentTheme } from "./utils";
import BeautifulInput from "./BeautifulInput";
import BeautifulButton from "./BeautifulButton";

function RegMain() {
  const style = getCurrentTheme("loginPage");
  return (
    <div style={style.loginMain}>
      <h2>Регистрация</h2>
      <BeautifulInput text="Имя пользователя" type="text" />
      <br />
      <BeautifulInput text="Email" type="text" /> <br />
      <BeautifulInput text="Пароль" type="password" /> <br />
      <BeautifulInput text="Повторите Пароль" type="password" /> <br />
      <div style={{ display: "inline-flex" }}>
        <BeautifulButton text="Продолжить" />
        <p>Забыли пароль?</p>
        <p>Войти</p>
      </div>
    </div>
  );
}
export default RegMain;
