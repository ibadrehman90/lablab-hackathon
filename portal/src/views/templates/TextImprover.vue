
<script setup>
import { ref, computed } from "vue";
const title = ref("")
const tone = ref("")
const content = ref();
const isData = ref(false)
const overlay = ref(false)
const color = ref("")
const text = ref("")
const items = ref(['General','Cloudways'])
const selectedBusiness = ref('')
const buss_id = ref('')
const snackbar = ref(false)
/* eslint-disable */
async function generateNormal(){
  if (selectedBusiness.value == 'Cloudways'){
      buss_id.value = '1'
    } else {
      buss_id.value = '0'
    }
  if (title.value && tone.value !== ''){
    overlay.value = true
    const textarea = document.getElementById("mainContent")
    /* eslint-disable */
    var len = textarea.value.length;
    var start = textarea.selectionStart;
    var end = textarea.selectionEnd;
    var sel = textarea.value.substring(start, end);
    await fetch('http://127.0.0.1:5000/contentimprover/content', {
    method: 'POST',
    body: JSON.stringify({
        text:title.value,
        tone:tone.value,
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
    content.value = data.data
    isData.value = true
    overlay.value = false
    var startPos = textarea.selectionStart;
    var endPos = textarea.selectionEnd;
    textarea.value = textarea.value.substring(0, endPos)
          + "\n"+data.data
          + textarea.value.substring(endPos, textarea.value.length);
  }).catch(function (error) {
    console.warn('Something went wrong.', error);
  });
  } else {
    snackbar.value = true
    color.value = 'red'
    text.value = 'Please fill all the fields.'
  }
    

  }

  async function rephraseText(){
    const textarea = document.getElementById("mainContent")
    var len = textarea.value.length;
    var start = textarea.selectionStart;
    var end = textarea.selectionEnd;
    var sel = textarea.value.substring(start, end);
    await fetch('https://asciii-backend.herokuapp.com/longform/rewrite-better-readability', {
    method: 'POST',
    body: JSON.stringify({
      text: sel
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
    console.log(data);
    textarea.value =  textarea.value.substring(0,start) + data.data + textarea.value.substring(end,len);
  }).catch(function (error) {
    console.warn('Something went wrong.', error);
  });
}

const wordCounter = computed(() => {
        return title.value.length
    })
</script>

<template>
  <div class="main">
      <v-container>
          <v-row>
              <v-col class="right" cols="6">
                <v-banner lines="two">
                    <template v-slot:prepend>
                    <v-avatar><v-icon icon="mdi-lead-pencil" size="x-large"></v-icon></v-avatar>
                    </template>
                    <v-banner-text>
                        <h3>Text Improver</h3>
                        <p>Re-writes & improves content</p>
                    </v-banner-text>
                </v-banner>
                <v-row class="first-row">
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                      <span style="margin-left:400px">{{wordCounter}}/1000</span>
                        <v-textarea v-model="title" maxlength="1000" label="Text" variant="outlined" placeholder="Write your content here..." rows="6"></v-textarea>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Sound like" v-model="tone"  variant="outlined" placeholder="E.g. Professional" density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="4"></v-col>
                    <v-col cols="4">
                        <v-btn color="primary" variant="tonal" @click="generateNormal()">Generate</v-btn>
                    </v-col>
                    <v-col cols="4"></v-col>
                </v-row>
              </v-col>
              <v-col cols="6">
                <!-- <v-banner lines="one" text="Output">
                  <p style="float:right">
                    <v-tooltip text="Highlight the text to rephrase it.">
                      <template v-slot:activator="{ props }">
                        <v-icon @click="rephraseText()" v-bind="props" icon="mdi-file-document-edit-outline" size="large"/>
                      </template>
                    </v-tooltip>
                  </p>
                </v-banner> -->
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
                  <v-textarea v-show="isData" id="mainContent" v-model="content" class="output" variant="filled" rows="22"></v-textarea>
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
.mdi-lead-pencil{
    color:#00C5CD;
}

.mdi-file-document-edit-outline{
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