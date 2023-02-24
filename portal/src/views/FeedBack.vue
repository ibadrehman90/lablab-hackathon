<script setup>
import { ref, computed } from "vue";
const feedback = ref("")
const template = ref()
const snackbar = ref(false)
const text = ref('')
const color = ref('')
/* eslint-disable */
async function sendFeedback () {
  await fetch('https://asciii-backend.herokuapp.com/user-feedback', {
    method: 'POST',
    body: JSON.stringify({
      name: localStorage.getItem('f_name'),
      template: template.value,
      feedback: feedback.value,
      u_id: localStorage.getItem('u_id')

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
        feedback.value = ''
        template.value = ''
        snackbar.value = true
        color.value = 'green'
        text.value = data.message
    }).catch(function (error) {
        snackbar.value = true
        color.value = 'red'
        text.value = 'Invalid username or password.'
        console.warn('Something went wrong.', error)
    });
}
/* eslint-disable */
const wordCounter = computed(() => {
    return feedback.value.length
})

</script>

<template>
  <div>
      <v-container>
        <v-row class="mid-row">
        <v-col cols="2"></v-col>
        <v-col cols="8">
            <v-card>
            <template v-slot:title>
                <v-icon class="ico" icon="mdi-pencil" />
                Feedback
            </template>
            <div class="form">
                <v-select
                v-model="template"
                clearable
                chips
                label="Chose template/templates"
                :items="['Blog Post', 'Text Blob Generator', 'Tone Detector', 'Content Improver', 'Commands', 'Converting Ad Copy', 'Blog IDeas', 'General']"
                variant="underlined"
            ></v-select>
            <span style="margin-left:620px">{{wordCounter}}/300</span>
            <v-textarea v-model="feedback" label="Your feedback..." maxlength="300"></v-textarea>
            <v-btn style="margin-bottom:20px;" variant="outlined" color="primary" @click="sendFeedback()"> Send </v-btn>
            </div>
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

.mid-row{
  margin-top:20px
}

.ico {
    margin-right:10px;
}

.form{
    width:90%;
    margin-left: 20px;
    text-align: center;
}

</style>