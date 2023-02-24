<script setup>
import { ref,onMounted } from "vue";
const fullname = ref("")
const email = ref("")
const skill = ref("5")
const isReached = ref(false)
const overlay = ref(true)
/* eslint-disable */
async function sendFeedback () {
  await fetch('https://asciii-backend.herokuapp.com/admin/users/usage', {
    method: 'POST',
    body: JSON.stringify({
      uid: localStorage.getItem('u_id')

    }),
    headers: {
        'Content-type': 'application/json; charset=UTF-8'
    }
    }).then(function (response) {
    if (response.ok) {
        return response.json();
    }
    return Promise.reject(response);
    }).then(function (data) {
        skill.value = data.usage / 20000 * 100
        if(skill.value > 90 && skill.value < 100){
            isReached.value = true
        }
        overlay.value = false
    }).catch(function (error) {
        console.warn('Something went wrong.', error)
    });
}
onMounted(() => {
  fullname.value = localStorage.getItem('f_name') + " " + localStorage.getItem('l_name')
  email.value = localStorage.getItem('email')
  sendFeedback()
});

</script>
<template>
    <div>
        <v-container>
          <v-row class="top-row">
          <v-col cols="2"></v-col>
          <v-col cols="8">
              <v-card>
              <template v-slot:title>
                  <v-icon class="ico" icon="mdi-account" />
                  Profile
              </template>
              <v-row>
                  <v-col cols="12" class="first">
                      <span >Name:</span>
                      <span class="txt">{{fullname}}</span>
                  </v-col>
              </v-row>
              <v-row class="mid-row">
                  <v-col cols="12" class="first">
                      <span >Email:</span>
                      <span class="txt">{{email}}</span>
                  </v-col>
              </v-row>
              <v-row class="mid-row">
                  <v-col cols="12" class="first">
                      <span >Plan:</span>
                      <span class="txt">Beta Trial (~20,000 word limit)</span>
                  </v-col>
              </v-row>
              <v-row class="mid-row">
              <v-col cols="10" class="first">
                  <span >Usage: </span>
                    <v-progress-linear class="usage" v-model="skill" color="blue-grey" height="25">
                    <template v-slot:default="{ value }">
                        <strong>{{ Math.ceil(value) }}%</strong>
                    </template>
                    </v-progress-linear>
              </v-col>
             </v-row>
             <v-row>
                 <v-col cols="6"></v-col>
                 <v-col cols="2">
                    <v-progress-circular class="loader" v-show="overlay" color="primary" indeterminate :size="53"></v-progress-circular>
                 </v-col>
                 <v-col cols="4"></v-col>
             </v-row>
             <v-row>
                 <v-col cols="5"></v-col>
                 <v-col cols="4">
                    <v-btn v-show="isReached" style="margin-bottom:20px;" variant="tonal" color="primary">Upgrade</v-btn>
                 </v-col>
                 <v-col cols="3"></v-col>
             </v-row>
             <v-overlay v-model="overlay"></v-overlay>
              </v-card>
          </v-col>
          <v-col cols="2"></v-col>
          </v-row>
          
        </v-container>
    </div>
    <div class="text-center ma-2">
      <v-snackbar :timeout="2000" v-model="snackbar" :color="color" elevation="24">
        {{ text }}
      </v-snackbar>
      </div>
  </template>
  
  
  <style scoped>
  
  .top-row{
    margin-top:40px
  }
  .mid-row{
    margin-top:-40px
  }
  
  .ico {
      margin-right:10px;
  }
  
  .form{
      width:90%;
      margin-left: 20px;
      text-align: center;
  }

  .first{
      padding:30px
  }

  .txt{
      margin-left: 10px;
      font-size: 1.1rem;
      font-weight: bold;
  }

  .usage{
    margin-top: 10px;
    font-size: 1.1rem;
    font-weight: bold;
  }
  
  </style>