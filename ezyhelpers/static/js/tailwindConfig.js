tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#2B59C3',
          50: '#E8F0FE',
          100: '#D6E2FD',
          200: '#B1C6FB',
          300: '#8BAAF9',
          400: '#668DF7',
          500: '#2B59C3',
          600: '#2247A0',
          700: '#1A357D',
          800: '#11235A',
          900: '#091137'
        },
        secondary: {
            DEFAULT: '#0075FF',
            50: '#F0F7FF',
            100: '#E5F1FF',
            200: '#C2DEFF',
            300: '#9ECAFF',
            400: '#7BB7FF',
            500: '#0075FF',
            600: '#0069E6',
            700: '#0052B3',
            800: '#003B80',
            900: '#00234D'
            },
        accent: {
          DEFAULT: '#E71D36',
          50: '#FDE8EB',
          100: '#FBD1D7',
          200: '#F7A3AF',
          300: '#F37588',
          400: '#EF4760',
          500: '#E71D36',
          600: '#B9162B',
          700: '#8B1020',
          800: '#5D0B15',
          900: '#2F050A'
        },
        dark: '#252525',
        light: '#F8F9FA',
        gray: {
          DEFAULT: '#6C757D',
          50: '#F8F9FA',
          100: '#E9ECEF',
          200: '#DEE2E6',
          300: '#CED4DA',
          400: '#ADB5BD',
          500: '#6C757D',
          600: '#495057',
          700: '#343A40',
          800: '#212529',
          900: '#16181A'
        }
      },
      fontFamily: {
        sans: ['"Open Sans"', 'sans-serif'],
        heading: ['"Poppins"', 'sans-serif'],
        display: ['"Montserrat"', 'sans-serif']
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-in-out',
        'slide-up': 'slideUp 0.6s ease-out',
        'slide-down': 'slideDown 0.6s ease-out',
        'slide-left': 'slideLeft 0.6s ease-out',
        'slide-right': 'slideRight 0.6s ease-out',
        'pulse-slow': 'pulse 4s infinite',
        'float': 'float 6s ease-in-out infinite',
        'float-reverse': 'floatReverse 6s ease-in-out infinite',
        'tilt': 'tilt 10s ease-in-out infinite',
        'wave': 'wave 8s ease-in-out infinite'
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' }
        },
        slideUp: {
          '0%': { transform: 'translateY(40px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        },
        slideDown: {
          '0%': { transform: 'translateY(-40px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        },
        slideLeft: {
          '0%': { transform: 'translateX(40px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' }
        },
        slideRight: {
          '0%': { transform: 'translateX(-40px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' }
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' }
        },
        floatReverse: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(20px)' }
        },
        tilt: {
          '0%, 100%': { transform: 'rotate(-2deg)' },
          '50%': { transform: 'rotate(2deg)' }
        },
        wave: {
          '0%': { transform: 'translateX(0)' },
          '50%': { transform: 'translateX(-10px)' },
          '100%': { transform: 'translateX(0)' }
        }
      }
    }
  }
}