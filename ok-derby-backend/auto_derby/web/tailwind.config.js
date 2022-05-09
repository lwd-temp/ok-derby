module.exports = {
  important: '#h',
  content: ['./src/**/*.{vue,ts}'],
  theme: {
    extend: {
      colors: {
        theme: {
          text: '#794016',
          green: '#99da08',
          toast: '#9da1b0',
        },
      },
      minHeight: {
        12: '3rem',
        16: '4rem',
        32: '8rem',
      },
    },
  },
  plugins: [require('@tailwindcss/forms')],
};
