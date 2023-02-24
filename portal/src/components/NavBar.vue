<script setup>
import { ref, onMounted } from "vue";
import router from "@/router";

const f_name = ref("")
const l_name = ref("")
const email = ref("")
const fullname = ref("")
/* eslint-disable */
function goDashboard() {
  router.push({ name: "dashboard" });
}

function goFeedback() {
  router.push({ name: "feedback" });
}

function goTemplates() {
  router.push({ name: "templates" });
}

function goOutputs() {
  router.push({ name: "outputs" });
}

function goSettings() {
  router.push({ name: "settings" });
}

onMounted(() => {
  f_name.value = localStorage.getItem('f_name')
  l_name.value = localStorage.getItem('l_name')
  fullname.value = f_name.value + " " + l_name.value
  email.value = localStorage.getItem('email')
});
</script>

<template>
 <v-list>
    <v-list-item
      prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg"
      :title=fullname
      :subtitle=email
    ></v-list-item>
</v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item class="ico" prepend-icon="mdi-view-dashboard-outline" title="Dashboard" value="dashboard" @click="goDashboard()"></v-list-item>
          <v-list-item class="ico" prepend-icon="mdi-folder" title="Templates" value="templates" @click="goTemplates()"></v-list-item>
          <v-list-item class="ico" prepend-icon="mdi-comment-edit-outline" title="Feedback" value="feedback" @click="goFeedback()"></v-list-item>
          <v-list-item class="ico" prepend-icon="mdi-account-multiple" title="Profile" value="profile" @click="goSettings()"></v-list-item>
        </v-list>
</template>

<style scoped>

.ico:hover{
    color: black;
    background-color: #00c6cd65;
}


</style>