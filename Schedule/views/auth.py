from django.shortcuts import render
# from django.urls import reverse
# from CalendarApp import settings
# from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


def auth(request, template_name):
    if not request.user.is_authenticated:
        user = authenticate(request)
        if user is not None:
            if user.is_active:
                login(request, user)
                print('login')
                return render(request, template_name)
    else:
        logout(request)
        print('logout')
        return render(request, template_name)
