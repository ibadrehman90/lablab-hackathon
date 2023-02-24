<template>
  <v-app>
    <v-navigation-drawer v-if="!$route.meta.hideNavbar" v-model="drawer">
     <NavBar />
    </v-navigation-drawer>
    <v-app-bar v-if="!$route.meta.hideTopbar">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title></v-toolbar-title>
      <v-btn
      variant="outlined"
      color="warning"
      @click="logout()"
      >
      Log out
    </v-btn>
    </v-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import { defineComponent } from 'vue'
import NavBar from '../src/components/NavBar.vue'
import router from "@/router";
export default defineComponent({
  name: 'App',
  components: {NavBar},
  data: () => (
    { drawer: null
    }),
    methods: {
      logout () {
        localStorage.removeItem('gghqw')
        localStorage.removeItem('f_name')
        localStorage.removeItem('l_name')
        localStorage.removeItem('email')
        localStorage.removeItem('u_id')
        localStorage.removeItem('plan_id')
        router.push({name : "login"})
      }
    }
})
</script>
