
const hideTab = document.getElementById("hide-tab");
const extractTab = document.getElementById("extract-tab");

const hideSection = document.getElementById("hide-section");
const extractSection = document.getElementById("extract-section");

hideTab.addEventListener("click", function () {

    hideSection.hidden = false;
    extractSection.hidden = true;

    hideTab.classList.add("active");
    extractTab.classList.remove("active");

});

extractTab.addEventListener("click", function () {

    extractSection.hidden = false;
    hideSection.hidden = true;

    extractTab.classList.add("active");
    hideTab.classList.remove("active");

});
