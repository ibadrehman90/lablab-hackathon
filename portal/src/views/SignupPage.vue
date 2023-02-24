<script setup>
import { ref} from "vue";
import router from "@/router";


const first = ref("")
const last = ref("")
const email = ref("")
const password = ref("")
const snackbar = ref(false)
const text = ref('')
const color = ref('')
/* eslint-disable */
async function userSignup(){
    await fetch('https://asciii-backend.herokuapp.com/register', {
    method: 'POST',
    body: JSON.stringify({
        first_name: first.value,
        last_name: last.value,
        email: email.value,
        password: password.value,
        token: '',
        plan_id: '1',
        custom_quota: '0.0'
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
    router.push({name : "login"})
    }).catch(function (error) {
    snackbar.value = true
    color.value = 'red'
    text.value = 'Something went wrong. Please try again.'
    console.warn('Something went wrong.', error)
    });

}

</script>

<template>

    <div>
        <v-container>
            <v-row class="loginCard">
                <v-col cols="7">
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
                <v-col class="loginBox" cols="5">
                    <v-card
                    class="mx-auto"
                    max-width="414"
                    title="User Registration"
                    >
                    <v-container>
                        <v-row>
                        <v-col cols="12" sm="6">
                            <v-text-field
                        v-model="first"
                        color="primary"
                        label="First name"
                        variant="underlined"
                    ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6">
                            <v-text-field
                        v-model="last"
                        color="primary"
                        label="Last name"
                        variant="underlined"
                    ></v-text-field>
                        </v-col>
                        </v-row>
                    

                    

                    <v-text-field
                        v-model="email"
                        color="primary"
                        label="Email"
                        variant="underlined"
                    ></v-text-field>

                    <v-text-field
                        v-model="password"
                        color="primary"
                        label="Password"
                        placeholder="Enter your password"
                        variant="underlined"
                        type="password"
                    ></v-text-field>

                    <v-text-field
                        v-model="conf_password"
                        color="primary"
                        label="Confirm password"
                        placeholder="Confirm password"
                        variant="underlined"
                        type="password"
                    ></v-text-field>

                    <v-checkbox color="primary" :label=label></v-checkbox>
                    </v-container>

                    <v-divider></v-divider>

                    <v-card-actions>
                    <v-spacer></v-spacer>

                    <v-btn color="secondary" @click="userSignup()">
                        Complete Registration
                    <v-icon icon="mdi-chevron-right" end></v-icon>
                    </v-btn>
                    </v-card-actions>
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
    margin-top: -40px;
}


</style>