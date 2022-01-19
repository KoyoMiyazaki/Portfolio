module.exports = {
  purge: {
    enabled: true,
    content: ["../accounts/templates/account/*.html"],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      body: [
        'Arial',
        'sans-serif',
      ],
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
