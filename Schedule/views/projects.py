from django.shortcuts import render
from .auth import auth
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def my_projects(request):
    template_name = "Schedule/my.html"
    print("GET", request.is_ajax())
    if request.method == "POST":
        if request.is_ajax():
            print("POST", request.is_ajax())
            auth(request, template_name)
    return render(request, template_name)


@ensure_csrf_cookie
def current_projects(request):
    template_name = "Schedule/current.html"
    print("GET", request.is_ajax())
    if request.method == "POST":
        if request.is_ajax():
            print("POST", request.is_ajax())
            auth(request, template_name)
    return render(request, template_name)


@ensure_csrf_cookie
def requests(request):
    template_name = "Schedule/requests.html"
    print("GET", request.is_ajax())
    if request.method == "POST":
        if request.is_ajax():
            print("POST", request.is_ajax())
            auth(request, template_name)
    return render(request, template_name)
