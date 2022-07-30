<template>
    <div class="page-layout">
        <div class="main-panel">
            <CodeEditor />
            <ConsoleOutput />
            <ConsoleInput />
        </div>
        <div class="side-panel">
            <GenericControls />
            <CodeControls />
        </div>
    </div>
</template>

<script>
import CodeEditor from "./editor/CodeEditor.vue";
import ConsoleOutput from "./editor/ConsoleOutput.vue";
import ConsoleInput from "./editor/ConsoleInput.vue";

import GenericControls from "./controls/GenericControls.vue";
import CodeControls from "./controls/CodeControls.vue";

export default {
    name: "PageLayout",
    props: {},
    components: {
        CodeEditor,
        ConsoleOutput,
        ConsoleInput,
        GenericControls,
        CodeControls,
    },
    data: () => {
        return {};
    },
    mounted() {},
    methods: {},
};
</script>

<style scoped>
.page-layout {
    display: flex;
    flex-direction: row;
    height: 100%;
}

.main-panel {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    height: 100%;
    width: 60vw;
}

.side-panel {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    height: 100%;
    width: 40vw;
}
</style>
