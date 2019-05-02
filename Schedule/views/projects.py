from django.shortcuts import render, redirect
from django.urls import reverse
from .auth import auth
from django.views.decorators.csrf import ensure_csrf_cookie
from ..models import Project, Request, UserInProject
from django.contrib.auth.models import User
from ..forms import CreateProjectForm
from django.contrib import messages


@ensure_csrf_cookie
def current_projects(request):
    template_name = "Schedule/current.html"
    # projects = Project.objects.all()
    user_in_projects = UserInProject.objects.all()
    print("GET")
    # print(Project.objects.get(title="Нічосі проектік").userinproject_set)
    if request.method == "POST":
        print("POST", request.POST)
        if "create_project" in request.POST:
            create_project(request, template_name, "current", user_in_projects)
    create_project_form = CreateProjectForm(user=request.user)
    return render(request, template_name, {"projects": user_in_projects,
                                           "create_project_form": create_project_form})
    # return render(request, template_name, {"projects": projects})


@ensure_csrf_cookie
def my_projects(request):
    template_name = "Schedule/my.html"
    user_projects = UserInProject.objects.filter(user=request.user)
    print("GET")
    if request.method == "POST":
        print("POST", request.POST)
        if "create_project" in request.POST:
            create_project(request, template_name, "my", user_projects)
    create_project_form = CreateProjectForm(user=request.user)
    return render(request, template_name, {"projects": user_projects,
                                           "create_project_form": create_project_form})


@ensure_csrf_cookie
def project_admin(request):
    template_name = "Schedule/project_admin.html"
    print("GET")
    if request.method == "POST":
        print("POST")
    return render(request, template_name)


@ensure_csrf_cookie
def requests(request):
    template_name = "Schedule/requests.html"
    request_projects = Request.objects.all()
    print("GET")
    if request.method == "POST":
        print("POST", request.POST)
        if "create_project" in request.POST:
            create_project(request, template_name, "requests", request_projects)
    create_project_form = CreateProjectForm(user=request.user)
    return render(request, template_name, {"projects": request_projects,
                                           "create_project_form": create_project_form})


def create_project(request, template_name, reverse_url, projects):
    create_project_form = CreateProjectForm(request.POST, user=request.user)
    if create_project_form.is_valid():
        print("submit")
        create_project_form.save()
        messages.success(request, "Заявка успішно відправлена", extra_tags="notify_active")
        return redirect(reverse(reverse_url))
    else:
        print("error render")
        return render(request, template_name, {"projects": projects,
                                               "create_project_form": create_project_form})


