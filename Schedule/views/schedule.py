from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from CalendarApp import settings
from django.shortcuts import redirect
# from apiclient import discovery
from httplib2 import Http
from django.contrib.auth.models import User
from google.oauth2 import service_account
import json
import datetime
import os
from django.views.decorators.csrf import ensure_csrf_cookie
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from ..forms import RequestForm
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


@ensure_csrf_cookie
def schedule(request):
    template_name = "Schedule/schedule.html"
    access_token = request.user.social_auth.get().access_token
    print("GET")
    if request.method == "POST":
        form = RequestForm(request.POST, service=get_api_service(access_token))
        # form = RequestForm(request.POST)
        print("POST", request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("schedule"))
        else:
            return render(request, template_name, {"form": form})
    form = RequestForm(service=get_api_service(access_token))
    # form = RequestForm()
    return render(request, template_name, {"form": form})


def get_api_service(access_token):
    # credentials = service_account.Credentials.from_service_account_file(
    #     settings.GOOGLE_CALENDAR_SECRETS_FILE, scopes=settings.GOOGLE_API_SCOPES)
    service = build('calendar', 'v3', credentials=Credentials(access_token))
    return service


def get_permission(request, provider):
    user_with_permission = request.user.social_auth.get(provider=provider)
    print(user_with_permission)
    return redirect(reverse("schedule"))
