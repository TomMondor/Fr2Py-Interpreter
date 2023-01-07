import { locEn } from "./loc-en";
import { locFr } from "./loc-fr";

//TODO use constants instead of strings 'fr' and 'en'
const languages = {
    fr: locFr,
    en: locEn,
};

const defaultLanguage = "fr";
export let selectedLanguage = defaultLanguage;

export const toggleSelectedLanguage = () => {
    selectedLanguage = selectedLanguage === "fr" ? "en" : "fr";
};

export const translate = (text) => {
    const textSegments = text.split("|").reverse();

    //TODO cleaner way to do this?
    try {
        let translated = languages[selectedLanguage][textSegments.pop()];
        while (textSegments.length > 0) {
            translated = translated[textSegments.pop()];
        }

        return translated;
    } catch (error) {
        return text.split("|").pop();
    }
};

//TODO store selected language in localStorage?
