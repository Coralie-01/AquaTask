/** @type {import('tailwindcss').Config} */
/* eslint-env node */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  purge: ['./src/**/*.{html,js,vue}',],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: [
      {
        base: {
          "primary": '#648767',
          "secondary": '#054A91',
          "accent": '#F03A47',
          "neutral": '#333c4d',
          "base-100": '#ffffff',
          "info": '#276FBF',
          "success": '#7FB685',
          "warning": '#FBC94B',
          "error": '#EE6055'
        }
      },"aqua","emerald" 
    ]
  },
}

