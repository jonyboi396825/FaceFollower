<template>
  <div id="root">
    <p> Press WASD to move the robot </p> 
    <p>{{msg}}</p>

  </div>
</template>

<script>
export default {
  name: "Index",
  el: "#root",
  data() {
    return {
      wisdown: false,
      aisdown: false,
      sisdown: false,
      disdown: false,
      msg: "asdf"
    };
  },
  methods: {
    goForwardStart: function(){
      console.log("Go forward");
    },
    goForwardStop: function(){
      console.log("Stop going forward");
    }
  },
  mounted() {    
    window.addEventListener("keydown", (e) => {
      e = e || window.event;

      if (e.key == 'w' && !this.wisdown){
          console.log("w down");
          this.wisdown = true;
        } 
      if (e.key == 'a' && !this.aisdown){
          console.log("a down");
        this.aisdown = true;
        }
      if (e.key == 's' && !this.sisdown){
          console.log("s down");
        this.sisdown = true;
        }
      if (e.key == 'd' && !this.disdown){
          console.log("d down");
        this.disdown = true;
        }
    });

    window.addEventListener("keyup", (e) => {
      e = e || window.event;

      if (e.key == 'w' && this.wisdown){
        console.log("w up");
          this.wisdown = false;
        }
      if (e.key == 'a' && this.aisdown){
          console.log("a up");
          this.aisdown = false;
        }
      if (e.key == 's' && this.sisdown){
          console.log("s up");
          this.sisdown = false;
        }
      if (e.key == 'd' && this.disdown){
          console.log("d up");
          this.disdown = false;
        } 
    });
  },
}

</script>


