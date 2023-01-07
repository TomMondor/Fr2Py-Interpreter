<template>
    <ControlsBox :title="translatedTitle">
        <IconButton iconName="languages" :onClick="onLanguageToggle" />
        <IconButton iconName="toggle-theme" :onClick="onToggleTheme" />
    </ControlsBox>
</template>

<script>
import { translate } from "../../assets/locales/localizationService";
import { toggleTheme } from "../../assets/theme/themeService";

import ControlsBox from "../reusables/ControlsBox.vue";
import IconButton from "../reusables/IconButton.vue";

export default {
    name: "GenericControls",
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
            return translate("controls|genericControls");
        },
    },
    mounted() {},
    methods: {
        onLanguageToggle() {
            // TODO
            // toggleSelectedLanguage();
            this.$toggleLanguage();
            // this.$forceUpdate();
        },
        onToggleTheme() {
            toggleTheme();
        },
    },
};
</script>

<style scoped></style>
