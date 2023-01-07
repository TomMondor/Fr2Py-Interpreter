<template>
    <!--  TODO afficher selon les props de lignes et colonnes. -->
    <div class="outer-container">
        <div class="top">
            <div class="left-corner"></div>
            <div class="title">{{ title }}</div>
            <div class="right-corner"></div>
        </div>
        <div class="inner-container">
            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: "ControlsBox",
    props: {
        title: String,
        maxRows: Number,
        maxColumns: Number,
    },
    components: {},
    data: () => {
        return {};
    },
    mounted() {},
    methods: {},
};
</script>

<style scoped>
* {
    --border-radius: 15px;
}

.outer-container {
    display: flex;
    flex-direction: column;
    width: fit-content;
}

.top {
    display: flex;
    flex-direction: row;
    width: 100%;
}

.left-corner {
    border-left: 3px solid var(--border-color);
    border-top: 3px solid var(--border-color);
    border-top-left-radius: var(--border-radius);
    min-width: 20px;
}

.title {
    position: relative;
    top: -7px;
    white-space: nowrap;
}

.right-corner {
    border-right: 3px solid var(--border-color);
    border-top: 3px solid var(--border-color);
    border-top-right-radius: var(--border-radius);
    width: 100%;
    min-width: 20px;
}

.inner-container {
    display: flex;
    flex-direction: row;
    gap: 8px;
    padding: 0px 8px 8px;
    border: 3px solid var(--border-color);
    border-top: none;
    border-bottom-right-radius: var(--border-radius);
    border-bottom-left-radius: var(--border-radius);
}
</style>
