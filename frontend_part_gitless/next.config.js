module.exports = require("next-compose-plugins")(
  [[require("next-images")], [require("next-fonts")]],
  {
    devIndicators: {
      autoPrerender: false,
    },
    reactStrictMode: true,
  },
);
