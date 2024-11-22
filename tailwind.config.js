/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./static/dist/**/*.js"],
  theme: {
    extend: {
      colors: {
        primary: "#EA580C",
        secondary: "#F9FAFC",
      },
      container: {
        center: true,
        padding: {
          DEFAULT: "1rem",
          sm: "1rem",
          lg: "1rem",
          xl: "1rem",
          "2xl": "6rem",
        },
      },
    },
  },
  plugins: [],
};
