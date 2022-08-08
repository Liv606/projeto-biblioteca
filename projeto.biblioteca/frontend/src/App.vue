<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: justify;
  color: white;
  margin-top: 60px;
}
body{
  background-color: #003B5C;
}
h1,p{
  text-align: center;
}
.table{
   margin: auto;
   border: 1;
}
.routerlink{
  display: block;
  color: black;
  font-weight: bold;
  ;
}
button{
    background-color: #B0C4DE;
    color: black;
    width: 200px;
}
</style>
