module.exports = {
  purge: [],
  theme: {
    extend: {
      inset: {
        '1/2': '50%',
        '2/3': '66%',
      },
      colors: {
        'bcg-gray-sidebar': '#333333',
        'bcg-green-first': '#177B57',
        'bcg-green-second': '#136749',
        'bcg-green-third': '#0F523A',
        'bcg-green-fourth': '#0C3E2C',
        'bcg-green-fifth': '#08291D',
        'bcg-green-sixth': '041150F',
        'bcg-green-seventh': '#000000',      
      },
      lineHeight: {
        'extra-loose': '2.5',
      },
      spacing: {
        '200': '50rem',
      },
      maxHeight: {
        '0': '0',
        '1/4': '25%',
        '1/2': '50%',
        '3/4': '75%',
        'full': '100%',
      }
    },
  },
  variants: {
    textColor: ['responsive', 'hover','focus', 'group-hover'],
  },
  plugins: [],
}
