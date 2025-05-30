module.exports = {
  content: [
    './src/**/*.{html,js,jsx,ts,tsx,vue}', // Путь к файлам внутри src
    './public/assets/**/*.{css}',  // Путь к файлам в public/assets
  ],
  theme: {
    extend: {
      colors: {
        primary: '#4c6ef5',
        secondary: '#f0f4f8',
        dark: '#1c1e29',
        light: '#f5f5f5',
        accent: '#ff5722',
        'hover-primary': '#3b5bbf',
        'focus-primary': '#2a3b9e',
        'active-primary': '#1f2a73',
        'dark-bg': '#121212',
        'dark-text': '#E5E5E5',
        'dark-button': '#4c6ef5',
      },
      fontFamily: {
        sans: ['Roboto', 'Arial', 'sans-serif'],
        serif: ['Georgia', 'serif'],
      },
      boxShadow: {
        custom: '0 4px 6px rgba(0, 0, 0, 0.1)',
      },
      spacing: {
        '128': '32rem',
      },
      borderRadius: {
        'xl': '1.5rem',
      },
      screens: {
        'xs': '480px',
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(circle, #ff7e5f, #feb47b)',
        'gradient-linear': 'linear-gradient(to right, #ff7e5f, #feb47b)',
      },
      animation: {
        'fade-in': 'fadeIn 1s ease-out forwards',
        'bounce-slow': 'bounce 3s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  darkMode: 'media', // для включения темной темы
  plugins: [],
  mode: 'jit'
};