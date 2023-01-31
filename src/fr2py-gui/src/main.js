import Vue from "vue";
import App from "./App.vue";

import { translate, toggleSelectedLanguage } from "./assets/locales/localizationService";

Vue.config.productionTip = false;

Vue.mixin({
    methods: {
        $translate: function (key) {
            return translate(key);
        },
        $toggleLanguage: function () {
            toggleSelectedLanguage();
            console.log("MIXIN");
            this.$forceUpdate(); //TODO rendu ici, ne semble pas affecter l'instance vue complète. Maybe utiliser un provider (qui wrap tt l'app)
        },
    },
});

new Vue({
    render: (h) => h(App),
}).$mount("#app");
