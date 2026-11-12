const menuToggle = document.getElementById("menuToggle");
const navMenu = document.getElementById("navMenu");

menuToggle.addEventListener("click", function () {
    navMenu.classList.toggle("open");
});

document.querySelectorAll("#navMenu a").forEach(function(link) {
    link.addEventListener("click", function() {
        navMenu.classList.remove("open");
    });
});