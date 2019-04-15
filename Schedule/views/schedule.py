from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from CalendarApp import settings
from django.shortcuts import redirect
from apiclient import discovery
from google.oauth2 import service_account
import json
import datetime
import os
# from .auth import auth
from django.views.decorators.csrf import ensure_csrf_cookie
# from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


@ensure_csrf_cookie
def schedule(request):
    template_name = "Schedule/schedule.html"
    print("GET", request.is_ajax())
    if request.method == "POST":
        print("POST")
        event = {
            'summary': 'Google I/O 2015',
            'location': '800 Howard St., San Francisco, CA 94103',
            'description': 'A chance to hear more about Google\'s developer products.',
            'start': {
                'dateTime': '2019-04-16T09:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': '2015-04-16T17:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'attendees': [],
        }
        event = get_api_service().events().insert(calendarId='primary', body=event).execute()
        print('Request send seccessfully')
    return render(request, template_name)


def get_api_service():
    credentials = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_CALENDAR_SECRETS_FILE, scopes=settings.GOOGLE_API_SCOPES)
    service = discovery.build('calendar', 'v3', credentials=credentials)
    return service
