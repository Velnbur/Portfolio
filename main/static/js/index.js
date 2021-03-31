function hover(element) {
    element.setAttribute("src", "static/img/menu-icon-hover.png");
    element.setAttribute("style", "background-color: white;");
}

function unhover(element) {
    element.setAttribute("src", "static/img/menu-icon.png");
    element.setAttribute("style", "background-color: transparent;");
}
