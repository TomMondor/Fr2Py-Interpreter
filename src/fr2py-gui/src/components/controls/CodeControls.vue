<template>
    <ControlsBox :title="translatedTitle">
        <IconButton iconName="play" :onClick="onRunClick" />
        <IconButton iconName="download" :onClick="onDownloadClick" />
        <IconButton iconName="upload" :onClick="onUploadClick" />
    </ControlsBox>
</template>

<script>
import { translate } from "../../assets/locales/localizationService";

import ControlsBox from "../reusables/ControlsBox.vue";
import IconButton from "../reusables/IconButton.vue";

export default {
    name: "CodeControls",
    props: {},
    components: {
        ControlsBox,
        IconButton,
    },
    data: () => {
        return {};
    },
    computed: {
        translatedTitle() {
            return translate("controls|codeControls");
        },
    },
    mounted() {},
    methods: {
        onRunClick() {
            //TODO
            console.log("onRunClick");
        },
        onDownloadClick() {
            //TODO
            console.log("onDownloadClick");
        },
        onUploadClick() {
            //TODO
            console.log("onUploadClick");
        },
    },
};
</script>

<style scoped></style>
