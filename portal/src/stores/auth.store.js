import { defineStore } from "pinia";

export const userAuth = defineStore("userauth", {
    id: "userauth",
    state: () => ({
      headlines: [],
      folds:[],
      isLoggedin: false,
      user: [{
        id: '',
        f_name: '',
        l_name: '',
        email: '',
        plan_id: ''
      }]
    }),
    getters: {
      doubleCount: (state) => state.count * 2,
    },
    actions: {
      userState (state) {
        if (state === 1) {
        this.isLoggedin = true
        } else {
            this.isLoggedin = false
        }
        return this.isLoggedin
      },

      setUserInfo (data) {
        this.user.id = data.u_id
        this.user.f_name = data.f_name
        this.user.l_name = data.l_name
        this.user.email = data.email
        this.user.plan_id = data.plan_id
      },

      fetchUser () {
        return this.user
      }
    },
  });