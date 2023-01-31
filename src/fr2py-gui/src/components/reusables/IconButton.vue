<template>
    <img
        class="icon-styling"
        :src="iconPath"
        :title="iconTooltip"
        :alt="iconTooltip"
        v-on:click="onClick"
    />
</template>

<script>
import { translate } from "../../assets/locales/localizationService";

export default {
    name: "IconButton",
    props: { iconName: String, onClick: Function },
    components: {},
    data: () => {
        return {};
    },
    computed: {
        iconPath() {
            return require("@/assets/icons/" + this.iconName + ".svg");
        },
        iconTooltip() {
            return translate(`icons|${this.iconName}`);
        },
    },
    mounted() {},
    methods: {},
};
</script>

<style scoped>
.icon-styling {
    height: 30px;
    cursor: pointer;
    color: var(--icon-color); /* TODO color doesn't seem to change */
    /* TODO make size responsive? */
}
</style>
