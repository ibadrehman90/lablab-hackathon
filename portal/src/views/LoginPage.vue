<script setup>
import { ref } from "vue";
import router from "@/router";

const email = ref('')
const password = ref('')
const snackbar = ref(false)
const text = ref('')
const color = ref('')

/* eslint-disable */
function goRegisterForm(){
    router.push({ name: "signup" });
}

async function userLogin(){
    await fetch('https://asciii-backend.herokuapp.com/login', {
    method: 'POST',
    body: JSON.stringify({
        email: email.value,
        password: password.value
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
        snackbar.value = true
        color.value = 'green'
        text.value = data.message
        localStorage.setItem('gghqw',data.access_token)
        localStorage.setItem('f_name',data.f_name)
        localStorage.setItem('l_name',data.l_name)
        localStorage.setItem('email',data.email)
        localStorage.setItem('u_id',data.u_id)
        localStorage.setItem('plan_id',data.plan_id)
        router.push({name : "dashboard"})
    }).catch(function (error) {
        snackbar.value = true
        color.value = 'red'
        text.value = 'Invalid username or password.'
        console.warn('Something went wrong.', error)
    });

}

</script>

<template>

    <div>
        <v-container>
            <v-row class="loginCard">
                <v-col cols="8">
                    <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material.jpg">
                        <div class="d-flex flex-column fill-height justify-center align-center text-white">
                            <h1 class="text-h4 font-weight-thin mb-4">
                                ASCIII.ai
                            </h1>
                            <h4 class="subheading">
                                AI Content for Humans
                            </h4>
                            <v-badge color="secondary" content="Beta v0.1.0" inline></v-badge>
                        </div>
                    </v-parallax>
                </v-col>
                <v-col class="loginBox" cols="4">
                    <v-card width="400">
                        <v-card-item style="padding:20px;text-align:center">
                            <v-card-title>Login</v-card-title>
                        </v-card-item>
                        <v-card-text>
                            <v-form>
                                <v-text-field
                                    clearable
                                    v-model="email"
                                    label="Username"
                                    prepend-icon="mdi-account"
                                    variant="outlined"
                                ></v-text-field>
                                <v-text-field
                                    clearable
                                    v-model="password"
                                    :rules="emailRules"
                                    label="Password"
                                    prepend-icon="mdi-key"
                                    variant="outlined"
                                    type="password"
                                ></v-text-field>
                            </v-form>
                        </v-card-text>
                        <div class="loginBtn">
                            <v-btn color="primary" @click="userLogin()">Login</v-btn>
                            <v-btn style="margin-left:10px" color="secondary" @click="goRegisterForm()">Register</v-btn>
                        </div>
                        
                    </v-card>
                </v-col>
                
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

.loginCard{
    margin-top: 150px;
}

.loginBtn{
    margin-left:10px;
    padding-top:5px;
    padding-bottom:20px;
    text-align: center;
}

.loginBox{
    margin-top: 60px;
}


</style>