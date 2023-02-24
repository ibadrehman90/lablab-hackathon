<script setup>
import router from "@/router";
/* eslint-disable */
function goBlogPost(){
  router.push({name: 'blogpost'})
}
function goTextBlob(){
  router.push({name: 'textblob'})
}
function goCommands(){
  router.push({name: 'commands'})
}
function goTextImprover(){
  router.push({name: 'textimprover'})
}
function goBlogOutline(){
  router.push({name: 'blogoutline'})
}
function goColdEmail(){
  router.push({name: 'coldemail'})
}
</script>

<template>
  <div class="main">
      <v-container>
          <v-row>
              <v-col md="3" xs="2">
                <v-card height="130" class="mx-auto" prepend-icon="mdi-file-document-edit-outline" @click="goBlogPost()">
                    <template v-slot:title>
                        <span class="title">Blog Post</span>
                    </template>
                    <v-card-text>
                    Suitable for 800 words
                    </v-card-text>
                </v-card>
              </v-col>
              <v-col md="3" xs="2">
                <v-card height="130" class="mx-auto" prepend-icon="mdi-file-document-outline" @click="goTextBlob()">
                    <template v-slot:title>
                    <span class="title">Text Blob Generator</span>
                    </template>
                    <v-card-text>
                    Generate a complete paragraph
                    </v-card-text>
                </v-card>
              </v-col>
              <v-col md="3" xs="2">
                <v-card height="130" class="mx-auto" prepend-icon="mdi-lead-pencil" @click="goTextImprover()">
                    <template v-slot:title>
                        <span class="title">Content Improver</span>
                    </template>
                    <v-card-text>
                    Re-writes & improves content
                    </v-card-text>
                </v-card>
              </v-col>
              <v-col md="3" xs="2">
                <v-card height="130" class="mx-auto" prepend-icon="mdi-message-minus-outline" @click="goCommands()">
                    <template v-slot:title>
                    <span class="title">Commands</span>
                    </template>
                    <v-card-text>
                    Be creative with commands
                    </v-card-text>
                </v-card>
              </v-col>
          </v-row>
          <v-row class="mid-row">
              <v-col md="3" xs="2">
                <v-card  height="130" class="mx-auto" prepend-icon="mdi-format-list-bulleted" @click="goBlogOutline()">
                    <template v-slot:title>
                        <span class="title">Blog Outline</span>
                    </template>
                    <v-card-text>
                    Generate SEO-optimized blog outline
                    </v-card-text>
                </v-card>
              </v-col>
              <v-col md="3" xs="2">
                <v-card height="130" class="mx-auto" prepend-icon="mdi-email-open-outline" @click="goColdEmail()">
                    <template v-slot:title>
                    <span class="title">Cold Email</span>
                    </template>
                    <v-card-text>
                      Effective cold emails with a compelling subject line.
                    </v-card-text>
                </v-card>
              </v-col>
          </v-row>
      </v-container>
  </div>
</template>

<style scoped>

.main {
    padding: 30px;
}

.title {
    font-size: 1.1rem !important;
}

.v-card:hover{
    cursor: pointer;
    border-bottom: 2px solid #00c6cd65;
    border-right: 2px solid #00c6cd65;
}

.disabled{
  color:lightgray;
}

.disabled:hover{
  cursor:default;
  border-bottom: 2px solid pink;
  border-right: 2px solid pink;
}

.mid-row {
    padding-top:40px
}

</style>