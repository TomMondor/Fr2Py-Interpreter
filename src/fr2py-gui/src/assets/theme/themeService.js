export const LIGHT_THEME = "light";
export const DARK_THEME = "dark";

let currentTheme = DARK_THEME;

const lightThemeValues = {
    "--background-color": "white",
    "--border-color": "black",
    "--text-color": "black",
    "--icon-color": "black",
};

const darkThemeValues = {
    "--background-color": "black",
    "--border-color": "white",
    "--text-color": "white",
    "--icon-color": "white",
};

/** Toggle theme from light to dark and vice versa */
export const toggleTheme = () => {
    currentTheme = currentTheme === LIGHT_THEME ? DARK_THEME : LIGHT_THEME;

    applyTheme();
};

const applyTheme = () => {
    const valuesToSet = currentTheme === LIGHT_THEME ? lightThemeValues : darkThemeValues;
    Object.entries(valuesToSet).forEach(([cssVar, color]) => {
        document.body.style.setProperty(cssVar, color);
    });
};
