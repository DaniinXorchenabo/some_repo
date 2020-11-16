import React from "react";
import ReactDOM from "react-dom";

import PageContentsForIndex from "./PageContentsForIndex";

it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(<PageContentsForIndex />, div);
  ReactDOM.unmountComponentAtNode(div);
});
