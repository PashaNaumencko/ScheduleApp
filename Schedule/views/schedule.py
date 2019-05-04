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
import datetime, time
import os
from django.views.decorators.csrf import ensure_csrf_cookie
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from social_django.utils import load_strategy
from ..forms import RequestForm
from django.contrib import messages
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


@ensure_csrf_cookie
def schedule(request):
    template_name = "Schedule/schedule.html"
    # access_token = request.user.social_auth.get().access_token
    print("GET")
    if request.method == "POST":
        access_token = get_google_oauth2_access_token(request.user)
        form = RequestForm(request.POST, service=get_api_service(access_token))
        # form = RequestForm(request.POST)
        print("POST", request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успішно відправлена", extra_tags="notify_active")
            return redirect(reverse("schedule"))
        else:
            return render(request, template_name, {"form": form})
    else:
        # form = RequestForm(service=get_api_service(access_token))
        form = RequestForm()
        return render(request, template_name, {"form": form})


def get_google_oauth2_access_token(user):
    social = user.social_auth.get(provider='google-oauth2')
    if social.extra_data['expires'] <= int(time.time()):
        strategy = load_strategy()
        social.refresh_token(strategy)
    return social.extra_data['access_token']


def get_api_service(access_token):
    # credentials = service_account.Credentials.from_service_account_file(
    #     settings.GOOGLE_CALENDAR_SECRETS_FILE, scopes=settings.GOOGLE_API_SCOPES)
    service = build('calendar', 'v3', credentials=Credentials(access_token))
    return service

