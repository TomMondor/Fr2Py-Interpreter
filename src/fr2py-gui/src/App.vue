<template>
    <div id="app">
        <PageLayout />
    </div>
</template>

<script>
import PageLayout from "./components/PageLayout.vue";

export default {
    name: "App",
    components: {
        PageLayout,
    },
};

import "./assets/theme/variables.css";
</script>

<style>
* {
    margin: 0;
    padding: 0;
}
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: var(--text-color);
    background-color: var(--background-color);
    width: 100vw;
    height: 100vh;
}
</style>
