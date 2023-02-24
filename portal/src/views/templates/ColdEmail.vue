<script setup>
import { ref } from "vue"
const title = ref("")
const tone = ref("")
const sender = ref("")
const recepient = ref("")
const descp = ref("")
const proposition = ref("")
const action = ref("")
const overlay = ref(false)
const color = ref("")
const text = ref("")
const snackbar = ref(false)
const email_subject = ref("")
const email_body = ref("")
/* eslint-disable */
async function generateIntro(){
    if (title.value && tone.value && sender.value && recepient.value && proposition.value && action.value && descp.value !== '') {
      overlay.value = true
      await fetch('https://hackathon-lablab.herokuapp.com/coldemail/subject', {
      method: 'POST',
      body: JSON.stringify({
        company: title.value,
        action: action.value,
        tone: tone.value
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
        email_subject.value = data.data
        writeCopy()
    }).catch(function (error) {
      console.warn('Something went wrong.', error);
    });
  } else {
    snackbar.value = true
    color.value = 'red'
    text.value = 'Please fill all the fields.'
  } 

}

async function writeCopy(){
        await fetch('https://hackathon-lablab.herokuapp.com/coldemail/body', {
        method: 'POST',
        body: JSON.stringify({
            recepient: recepient.value,
            company: title.value,
            product: descp.value,
            action: action.value,
            proposition: proposition.value,
            tone: tone.value,
            sender: sender.value
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
        email_body.value = data.data
        overlay.value = false
      }).catch(function (error) {
        console.warn('Something went wrong.', error);
      });
    }
</script>

<template>
    <div class="main">
        <v-container>
            <v-row>
                <v-col class="right" cols="6">
                <v-banner lines="two">
                    <template v-slot:prepend>
                    <v-avatar><v-icon icon="mdi-email-open-outline" size="x-large"></v-icon></v-avatar>
                    </template>
                    <v-banner-text>
                        <h3>Cold Email</h3>
                        <p>Effective cold emails with a compelling subject line.</p>
                    </v-banner-text>
                </v-banner>
                <v-row class="first-row">
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Company name" v-model="title"  variant="outlined" density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Product/service" v-model="descp"  variant="outlined" placeholder="E.g. web development agency." density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Recepient" v-model="recepient"  variant="outlined" density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-textarea v-model="action" maxlength="500" label="Action/intent" placeholder="E.g. Convince the client to revamp their website..." variant="outlined" rows="2"></v-textarea>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Proposition" v-model="proposition"  variant="outlined" placeholder="E.g. 20% off on all digital services..." density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Sender" v-model="sender"  variant="outlined" density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Sound like" v-model="tone" placeholder="Eg, Professional"  variant="outlined" density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="4"></v-col>
                    <v-col cols="4">
                        <v-btn color="primary" variant="tonal" @click="generateIntro()">Generate</v-btn>
                    </v-col>
                    <v-col cols="4"></v-col>
                </v-row>
                </v-col>
                <v-col cols="6">
                <v-banner lines="one" text="Output">
                </v-banner>
                <div class="inputArea">
                    <p class="headline">{{email_subject}}</p>
                    <p class="output">{{email_body}}</p>
                    <v-progress-circular class="loader" v-show="overlay" color="primary" indeterminate :size="53"></v-progress-circular>
                </div>
                <v-overlay v-model="overlay"></v-overlay>
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
    .mdi-email-open-outline{
        color:#00C5CD;
    }
    
    .mdi-note-plus-outline{
        color:#00C5CD;
        padding-left:20px
    }
    
    .right {
        border-right: 1px solid lightgray;
        height: 100vh;
    }
    
    .first-row {
        margin-top: 20px;
    }
    
    .mid-row {
        margin-top: 1px;
    }
    
    .output {
      margin-top:15px;
      padding:10px;
      line-height: 1.9rem;
      font-size: 1.2rem;
      white-space: pre-line;
    }

    .headline {
      margin-top:40px;
      font-weight: bold;
      padding:10px;
      line-height: 1.9rem;
      font-size: 1.2rem;
      white-space: pre-line;
    }
    
    .inputArea{
      height: 90vh;
      overflow: scroll;
    }
    
    .loader{
      position: fixed;
      top:40%;
      left: 75%;
    }
    
    </style>