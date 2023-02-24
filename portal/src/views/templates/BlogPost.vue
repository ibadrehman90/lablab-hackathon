<script setup>
import { ref } from "vue";
  const title = ref("");
  const kw = ref("");
  const tone = ref("");
  const audience = ref("");
  const content = ref();
  const intro= ref();
  const body = ref();
  const conclusion = ref();
  const isMetaMD = ref(false)
  const outline = ref("")
  const isData = ref(false)
  const overlay = ref(false)
  const color = ref("")
  const text = ref("")
  const snackbar = ref(false)

/* eslint-disable */

  async function generateIntro(){
    if (title.value && tone.value && kw.value && audience.value !== '') {
      isMetaMD.value = true
      overlay.value = true
      const textarea = document.getElementById("mainContent")
      var len = textarea.value.length;
      var start = textarea.selectionStart;
      var end = textarea.selectionEnd;
      var sel = textarea.value.substring(start, end);
      await fetch('http://127.0.0.1:5000/blogpost/intro', {
      method: 'POST',
      body: JSON.stringify({
          title:title.value,
          tone: tone.value,
          audience: audience.value
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
      intro.value = data
      generateOutline()
    }).catch(function (error) {
      console.warn('Something went wrong.', error);
    });
  } else {
    snackbar.value = true
    color.value = 'red'
    text.value = 'Please fill all the fields.'
  }
    

  }

  async function generateOutline(){
    await fetch('http://127.0.0.1:5000/blogpost/outline', {
    method: 'POST',
    body: JSON.stringify({
        title:title.value
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
    outline.value = data
    generateBody()
  }).catch(function (error) {
    console.warn('Something went wrong.', error);
  });
  }

  async function generateBody(){
    const textarea = document.getElementById("mainContent")
    var len = textarea.value.length;
    var start = textarea.selectionStart;
    var end = textarea.selectionEnd;
    var sel = textarea.value.substring(start, end);
    await fetch('http://127.0.0.1:5000/blogpost/body', {
    method: 'POST',
    body: JSON.stringify({
        title:title.value,
        outline:outline.value,
        keyword:kw.value
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
    body.value = data
    generateConclusion()
  }).catch(function (error) {
    console.warn('Something went wrong.', error);
  });

  }

  async function generateConclusion(){
    const textarea = document.getElementById("mainContent")
    var len = textarea.value.length;
    var start = textarea.selectionStart;
    var end = textarea.selectionEnd;
    var sel = textarea.value.substring(start, end);
    await fetch('http://127.0.0.1:5000/blogpost/conclusion', {
    method: 'POST',
    body: JSON.stringify({
        title:title.value,
        audience: audience.value,
        keyword:kw.value
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
    conclusion.value = data
    showText()
  }).catch(function (error) {
    console.warn('Something went wrong.', error);
  });

  }

  function showText(){
      content.value = "Introduction: \n\n"+intro.value + "\n\nBody: \n\n" + body.value + "\n\nConclusion \n\n" + conclusion.value
      isData.value = true
      overlay.value = false
  }
</script>

<template>
  <div class="main">
      <v-container>
          <v-row>
              <v-col class="right" cols="6">
                <v-banner lines="two">
                    <template v-slot:prepend>
                    <v-avatar><v-icon icon="mdi-file-document-edit-outline" size="x-large"></v-icon></v-avatar>
                    </template>
                    <v-banner-text>
                        <h3>Blog Post</h3>
                        <p>Generates a complete blog post with very minimum inputs.</p>
                    </v-banner-text>
                </v-banner>
                <v-row class="first-row">
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Blog title" v-model="title" variant="outlined" density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Keywords" v-model="kw" variant="outlined" density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Sound like" placeholder="E.g. Professional" v-model="tone" variant="outlined" density="compact"></v-text-field>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <v-text-field label="Audience" placeholder="E.g. Marketers" v-model="audience" variant="outlined" density="compact"></v-text-field>
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
  margin-top:40px
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