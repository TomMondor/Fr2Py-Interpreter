<template>
    <div class="code-editor">{{ translate("editor|title") }}</div>
</template>

<script>
import { translate } from "../../assets/locales/localizationService";

export default {
    name: "CodeEditor",
    props: {},
    components: {},
    data: () => {
        return {};
    },
    mounted() {},
    methods: { translate },
};
</script>

<style scoped>
.code-editor {
    display: flex;
    width: 50vw;
    height: 40vh;
    border: 1px solid rgb(0, 0, 0);
    border-radius: 4px;
}
</style>
