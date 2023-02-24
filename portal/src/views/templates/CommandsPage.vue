<script setup>
    import { ref, computed } from "vue"
    const prompt = ref("")
    const command = ref("")
    const ad_headline = ref("")
    const isMetaMD = ref(false)
    const isData = ref(false)
    const overlay = ref(false)
    const color = ref("")
    const text = ref("")
    const snackbar = ref(false)

    /* eslint-disable */
    async function generateNormal(){
        if (command.value !== '') {
            isMetaMD.value = true
        overlay.value = true
        await fetch('https://hackathon-lablab.herokuapp.com/commands/content', {
        method: 'POST',
        body: JSON.stringify({
            prompt: prompt.value,
            commands: command.value
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
        isMetaMD.value = false
        isData.value = true
        overlay.value = false
        
      }).catch(function (error) {
        console.warn('Something went wrong.', error);
      });
    } else {
        snackbar.value = true
        color.value = 'red'
        text.value = 'Filling the command field is required.'
    }
       
    
      }
    const wordCounter = computed(() => {
        return prompt.value.length
    })
    const commandCounter = computed(() => {
        return command.value.length
    })
    </script>
<template>
    <div class="main">
      <v-container>
          <v-row>
              <v-col class="right" cols="6">
                <v-banner lines="two">
                    <template v-slot:prepend>
                    <v-avatar><v-icon icon="mdi-message-minus-outline" size="x-large"></v-icon></v-avatar>
                    </template>
                    <v-banner-text>
                        <h3>Commands</h3>
                        <p>Generate any output with custom command for any input.</p>
                    </v-banner-text>
                </v-banner>
                <v-row class="first-row">
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <span style="margin-left:400px">{{commandCounter}}/500</span>
                        <v-textarea v-model="command"  maxlength="500" label="Command" variant="outlined" placeholder="Type your command here..." rows="2"></v-textarea>
                    </v-col>
                    <v-col cols="1"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="1"></v-col>
                    <v-col cols="10">
                        <span style="margin-left:400px">{{wordCounter}}/1500</span>
                        <v-textarea v-model="prompt"  maxlength="1500" label="Context" variant="outlined" placeholder="Add background information here..." rows="3"></v-textarea>
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
                <v-banner lines="one" text="Output">
                </v-banner>
                <div class="inputArea">
                  <v-textarea v-show="isData" v-model="ad_headline" class="output" variant="outline" readonly rows="22"></v-textarea>
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

.mdi-message-minus-outline{
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
  height: 80vh;
}

.loader{
  position: fixed;
  top:40%;
  left: 75%;
}

</style>