function hoverIn(element) {
    element.setAttribute("src", "/static/img/menu-icon-hover.png");
    element.setAttribute("style", "background-color: white;");
}

function hoverOut(element) {
    element.setAttribute("src", "/static/img/menu-icon.png");
    element.setAttribute("style", "background-color: transparent;");
}

function sidebarOpen() {
    document.getElementById("sidebar").style.display = "block";
    document.getElementById("button-sidebar").onclick = sidebarClose;
}

function sidebarClose() {
    document.getElementById("sidebar").style.display = "none";
    document.getElementById("button-sidebar").onclick = sidebarOpen;
}
