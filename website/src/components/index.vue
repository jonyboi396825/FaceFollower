<template>
  <div id="root">
    <p> Press WASD to move the robot </p> 

    <span type="button" v-if="wisdown" id="forwardbutton">Forward</span>
    <span type="button" v-if="aisdown" id="leftbutton">Left</span>
    <span type="button" v-if="sisdown" id="downbutton">Back</span>
    <span type="button" v-if="disdown" id="rightbutton">Right</span>

    <p>Last button press: {{lastUsed}}</p>

  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "Index",
  el: "#root",
  data() {
    return {
      wisdown: false,
      aisdown: false,
      sisdown: false,
      disdown: false,
      maxspeed: 127,
      lastUsed: Date.now()
    };
  },
  methods: {
    goForwardStart: function(){
        axios.post("http://raspberrypizero.local:7123/send", {
          data: `l:${this.maxspeed};r:${this.maxspeed}`,
          ending: "\n",
        }).then((res) => {
          console.log(res);
        }).catch((err) => {
          console.log(err.response);
        });
    },
    goLeftStart: function(){
        axios.post("http://raspberrypizero.local:7123/send", {
          data: `l:${-this.maxspeed};r:${this.maxspeed}`,
          ending: "\n",
        }).then((res) => {
          console.log(res);
        }).catch((err) => {
          console.log(err.response);
        });
    },
    goRightStart: function(){
        axios.post("http://raspberrypizero.local:7123/send", {
          data: `l:${this.maxspeed};r:${-this.maxspeed}`,
          ending: "\n",
        }).then((res) => {
          console.log(res);
        }).catch((err) => {
          console.log(err.response);
        });
    },
    goBackStart: function(){
        axios.post("http://raspberrypizero.local:7123/send", {
          data: `l:${-this.maxspeed};r:${-this.maxspeed}`,
          ending: "\n",
        }).then((res) => {
          console.log(res);
        }).catch((err) => {
          console.log(err.response);
        });
    },
    stop: function(){
      setTimeout(() => { 
        axios.post("http://raspberrypizero.local:7123/send", {
          data: "l:0;r:0",
          ending: "\n",
        }).then((res) => {
          console.log(res);
        }).catch((err) => {
          console.log(err.response);
        });
      }, 100);
    },
  },
  mounted() {    
    window.addEventListener("keydown", (e) => {
      e = e || window.event;

      // only one key at a time pressed
      if (this.wisdown || this.aisdown || this.sisdown || this.disdown) return;

      // return if time delay has not been 1 second
      if (Date.now() - this.lastUsed < 500) return;

      if (e.key == 'w' && !this.wisdown){
          console.log("w down");
          this.lastUsed = Date.now();
          this.goForwardStart();
          this.wisdown = true;
        } 
      if (e.key == 'a' && !this.aisdown){
          console.log("a down");
          this.lastUsed = Date.now();
          this.goLeftStart();
        this.aisdown = true;
        }
      if (e.key == 's' && !this.sisdown){
          console.log("s down");
          this.lastUsed = Date.now();
          this.goBackStart();
        this.sisdown = true;
        }
      if (e.key == 'd' && !this.disdown){
          console.log("d down");
          this.lastUsed = Date.now();
          this.goRightStart();
        this.disdown = true;
        }
    });

    window.addEventListener("keyup", (e) => {
      e = e || window.event;

      // return if time delay has not been 1 second
      /* if (Date.now() - this.lastUsed < 500) return; */

      if (e.key == 'w' && this.wisdown){
        console.log("w up");
          this.lastUsed = Date.now();
          this.stop();
          this.wisdown = false;
        }
      if (e.key == 'a' && this.aisdown){
          console.log("a up");
          this.lastUsed = Date.now();
          this.stop();
          this.aisdown = false;
        }
      if (e.key == 's' && this.sisdown){
          console.log("s up");
          this.lastUsed = Date.now();
          this.stop();
          this.sisdown = false;
        }
      if (e.key == 'd' && this.disdown){
          console.log("d up");
          this.lastUsed = Date.now();
          this.stop();
          this.disdown = false;
        } 
    });
  },
}

</script>


