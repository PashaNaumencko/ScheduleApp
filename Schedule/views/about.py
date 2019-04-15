from django.shortcuts import render
from .auth import auth
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def about(request):
    template_name = "Schedule/about.html"
    print("GET", request.is_ajax())
    if request.method == "POST":
        if request.is_ajax():
            print("POST", request.is_ajax())
            auth(request, template_name)
    return render(request, template_name)
