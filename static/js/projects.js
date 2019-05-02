const createProjectWindow = document.getElementById("createProjectOpen");
const createProjectButton = document.getElementById("createProjectButton");
const links = document.querySelectorAll(".projects-nav__link");

createProjectButton.addEventListener("click", function () {
    createProjectWindow.classList.add("show");
});

document.getElementById("createProjectClose").addEventListener("click", function(event) {
    createProjectWindow.classList.remove("show");
});

for (var link of links) {
    if (link.href === window.location.href) {
        link.classList.add("active");
    }
    else {
        link.classList.remove("active");
    }
}

window.addEventListener("click", function(event) {
    if (event.target === createProjectWindow) {
        createProjectWindow.classList.remove("show");
    }
});

(function () {
    var projectFormErrors = document.getElementById('createProjectFormErrors');
    var notifyMessage = document.getElementById('notifyMessage');

    if (projectFormErrors) {
        createProjectWindow.classList.add("show");
    }
    if (notifyMessage) {
        setTimeout(function () {
            notifyMessage.classList.add('notify_hide');
        }, 5000);
    }
})();

