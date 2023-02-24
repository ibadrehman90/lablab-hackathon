// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Vuetify
import { createVuetify, ThemeDefinition } from 'vuetify'

const myCustomLightTheme: ThemeDefinition = {
  dark: false,
  colors: {
    background: '#FFFFFF',
    surface: '#FFFFFF',
    primary: '#00C5CD',
    'primary-darken-1': '#3700B3',
    secondary: '#000000',
    'secondary-darken-1': '#018786',
    error: '#B00020',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FB8C00',
  }
}

export default createVuetify({
  theme: {
    defaultTheme: 'myCustomLightTheme',
    themes: {
      myCustomLightTheme,
    }
  }
  // icons: {
  //   defaultSet: 'mdi',
  //   aliases,
  //   sets: {
  //     fa,
  //     mdi,
  //   }
  // }
}
)

// useful links https://next.vuetifyjs.com/en/features/theme/
// https://next.vuetifyjs.com/en/features/global-configuration/