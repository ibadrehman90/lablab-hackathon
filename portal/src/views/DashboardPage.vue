<script setup>
import {onMounted } from "vue";


onMounted(() => {
  // console.log(vulStore.data[2].name);
  console.log(localStorage.getItem('u_id'))
});
</script>

<template>
  <v-container>
    <v-row class="top-row">
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-card>
          <template v-slot:title>
            <v-icon icon="mdi-information-outline" />
            Welcome
          </template>
          <v-card-text>
            <p class="maintxt">This is a beta release of the platform that is continuously developing, monitoring, and improving. Therefore, you might experience a few glitches or unexpected behavior quite frequently. If you encounter anything unusual or wish to report a bug or improvement, feel free to let us know through the <strong>Feedback</strong> option. </p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>

    <v-row class="mid-row">
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-card>
          <template v-slot:title>
            <v-icon icon="mdi-information-outline" />
            Terms & Conditions
          </template>
          <v-card-text>
            <p class="maintxt">Please bear in mind that this platform only generates the content it's requested for. As a user, it is your responsibility to refrain from trying to generate unethical, racial, violent, or offensive content. A significant discount is also offered to all selected beta users for fair usage of credits. Sharing credentials is also not allowed. Please use the tool and help us improve further. Thank You </p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
  </v-container>
</template>


<style>

.top-row{
  margin-top:20px
}

.mid-row{
  margin-top:20px
}

.maintxt{
  padding:10px;
  font-size:1.0rem;
  line-height: 1.4rem;
}


</style>