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

const uploadButton = document.getElementById('projectDocUploadButton');
const projectDocInput = document.getElementById('projectDocInput');
const fileInfo = document.querySelector('.file-input__info');

uploadButton.addEventListener('click', function (event) {
    // event.preventDefault();
    projectDocInput.click();
});

projectDocInput.addEventListener('change', function (event) {
    const name = projectDocInput.value.split(/\\|\//).pop();
    fileInfo.innerHTML = name.length > 20 ? name.substr(name.length - 20) : name;
});

