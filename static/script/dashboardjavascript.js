const sideButton = document.querySelector("#sidebar-menu-icon");
const sidebar = document.querySelector(".dashboard-sidebar");
const searchButton = document.querySelector("#dashboard-search-icon");

sideButton.onclick= function() {
    sidebar.classList.toggle("active");
};

searchButton.onclick = function() {
    sidebar.classList.toggle("active")
}

/* function menuOpenClose() {
    sidebar.toggle("active");
};

sideButton.addEventListener('onclick', menuOpenClose());
*/