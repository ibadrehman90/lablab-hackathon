import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import vuetify from './plugins/vuetify'
import VueCookies from 'vue-cookies'
import { loadFonts } from './plugins/webfontloader'

loadFonts()
const pinia = createPinia()

createApp(App)
  .use(router)
  .use(pinia)
  .use(vuetify)
  .use(VueCookies)
  .mount('#app')
