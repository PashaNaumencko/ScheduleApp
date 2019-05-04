from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .auth import auth
from django.views.decorators.csrf import ensure_csrf_cookie
from ..models import Project, Request
from django.contrib.auth.models import User
from ..forms import CreateProjectForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@ensure_csrf_cookie
def current_projects(request):
    template_name = "Schedule/current.html"
    projects = Project.objects.all()
    print("GET")
    if request.method == "POST":
        print("POST", request.POST)
        if "create_project_request" in request.POST:
            return create_project_request(request, template_name, "current", projects)
    else:
        create_project_form = CreateProjectForm(user=request.user)
        return render(request, template_name, {"projects": projects,
                                               "create_project_form": create_project_form})
    # return render(request, template_name, {"projects": projects})


@ensure_csrf_cookie
def my_projects(request):
    template_name = "Schedule/my.html"
    user_projects = Project.objects.filter(participants=request.user)
    print("GET")
    if request.method == "POST":
        print("POST", request.POST)
        if "create_project_request" in request.POST:
            return create_project_request(request, template_name, "my", user_projects)
        elif "delete_project" in request.POST:
            return delete_project(request, "my")
    else:
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


def requests(request):
    template_name = "Schedule/requests.html"

    request_projects = Request.objects.all()

    # request_projects_list = Request.objects.all()
    # paginator = Paginator(request_projects_list, 5)
    # page = request.GET.get('page')
    #
    # try:
    #     request_projects = paginator.page(page)
    # except PageNotAnInteger:
    #     request_projects = paginator.page(1)
    # except EmptyPage:
    #     request_projects = paginator.page(paginator.num_pages)

    print("GET")

    if request.method == "POST":
        print("POST", request.POST)
        if "create_project_request" in request.POST:
            return create_project_request(request, template_name, "requests", request_projects)
        elif "create_project" in request.POST:
            return create_project(request, "requests")
        elif "delete_project_request" in request.POST:
            return delete_project_request(request, "requests")
    else:
        create_project_form = CreateProjectForm(user=request.user)
        return render(request, template_name, {"projects": request_projects,
                                               "create_project_form": create_project_form})


def create_project_request(request, template_name, reverse_url, projects):
    print(request)
    create_project_form = CreateProjectForm(request.POST, user=request.user)
    if create_project_form.is_valid():
        print("create_project_request submit")
        create_project_form.save()
        messages.success(request, "Заявка успішно відправлена", extra_tags="notify_active")
        print(reverse_url)
        return redirect(reverse(reverse_url))
    else:
        print("error render")
        return render(request, template_name, {"projects": projects,
                                               "create_project_form": create_project_form})


def create_project(request, reverse_url):
    print("create_project submit")
    project_request = Request.objects.get(pk=request.POST["request_id"])
    new_project = Project.objects.create(title=project_request.title, description=project_request.description,
                                         admin=project_request.admin)
    new_project.participants.add(project_request.admin)
    project_request.delete()
    messages.success(request, "Проект успішно створений", extra_tags="notify_active")
    print(reverse_url)
    return redirect(reverse(reverse_url))


def delete_project_request(request, reverse_url):
    print("delete_project_request submit")
    project_request = Request.objects.get(pk=request.POST["request_id"])
    project_request.delete()
    messages.success(request, "Заявка відхилена", extra_tags="notify_active")
    return redirect(reverse(reverse_url))


def delete_project(request, reverse_url):
    print("delete_project submit")
    project_request = Project.objects.get(pk=request.POST["project_id"])
    project_request.delete()
    messages.success(request, "Проект успішно видалений", extra_tags="notify_active")
    return redirect(reverse(reverse_url))
