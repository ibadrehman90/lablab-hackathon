<script setup>
import { ref } from "vue"
const items = ref(['General','Cloudways'])
const selectedBusiness = ref('')
const ad_headline = ref("")
const title = ref("")
const audience = ref("")
const overlay = ref(false)
const color = ref("")
const text = ref("")
const buss_id = ref('')
const snackbar = ref(false)
/* eslint-disable */
async function generateIntro(){
    if (selectedBusiness.value == 'Cloudways'){
        buss_id.value = '1'
      } else {
        buss_id.value = '0'
    }
    if (title.value && audience.value !== '') {
      overlay.value = true
      await fetch('http://127.0.0.1:5000/article/outline', {
      method: 'POST',
      body: JSON.stringify({
        title: title.value,
        audience: audience.value,
        buss_id: buss_id.value
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
      ad_headline.value = data.data
      overlay.value = false
    }).catch(function (error) {
      console.warn('Something went wrong.', error);
    });
  } else {
    snackbar.value = true
    color.value = 'red'
    text.value = 'Please fill all the fields.'
  } 

}
</script>

<template>
<div class="main">
    <v-container>
        <v-row>
            <v-col class="right" cols="6">
            <v-banner lines="two">
                <template v-slot:prepend>
                <v-avatar><v-icon icon="mdi-format-list-bulleted" size="x-large"></v-icon></v-avatar>
                </template>
                <v-banner-text>
                    <h3>Blog Post Outline</h3>
                    <p>Brainstorm and generates outline for blog post.</p>
                </v-banner-text>
            </v-banner>
            <v-row class="first-row">
                <v-col cols="1"></v-col>
                <v-col cols="10">
                    <v-text-field label="Blog post title/topic" v-model="title"  variant="outlined" density="compact"></v-text-field>
                </v-col>
                <v-col cols="1"></v-col>
            </v-row>
            <v-row>
                <v-col cols="1"></v-col>
                <v-col cols="10">
                    <v-text-field label="Target audience" v-model="audience"  variant="outlined" placeholder="E.g. Home owners" density="compact"></v-text-field>
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
              <div style="height:74px;border-bottom:1px solid lightgrey;">
                  <span>Output</span>
                  <v-select 
                      style="width:50%;float:right;"
                      v-model="selectedBusiness"
                      :items="items"
                      label="Profile"
                      density="compact"
                    ></v-select>
                </div>
            <div class="inputArea">
                <!-- <p class="output">{{ad_headline}}</p> -->
                <div class="output" v-html="ad_headline"></div>
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
.mdi-format-list-bulleted{
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
  margin-top:40px;
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