import dark from "./dark";
const getCurrentTheme = (path: string) => {
  const position = path.indexOf("/") + 1;
  const module = path.slice(position);
  console.warn(path);
  return dark[module];
};
export { getCurrentTheme };
