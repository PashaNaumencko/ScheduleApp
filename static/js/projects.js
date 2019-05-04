(function () {
    const createProjectWindow = document.getElementById("createProjectOpen");
    const createProjectButton = document.getElementById("createProjectButton");
    const links = document.querySelectorAll(".projects-nav__link");
    const projectFormErrors = document.getElementById('createProjectFormErrors');
    const notifyMessage = document.getElementById('notifyMessage');

    createProjectButton.addEventListener("click", function () {
        createProjectWindow.classList.add("show");
    });

    document.getElementById("createProjectClose").addEventListener("click", function() {
        createProjectWindow.classList.remove("show");
    });

    window.addEventListener("click", function(event) {
        if (event.target === createProjectWindow) {
            createProjectWindow.classList.remove("show");
        }
    });

    for (let link of links) {
        if (link.href === window.location.href || link.href === window.location.href.slice(0, -1)) {
            link.classList.add("active");
        }
        else {
            link.classList.remove("active");
        }
    }

    if (projectFormErrors) {
        createProjectWindow.classList.add("show");
    }
    if (notifyMessage) {
        setTimeout(function () {
            notifyMessage.classList.add('notify_hide');
        }, 5000);
    }

})();


