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
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


@ensure_csrf_cookie
def schedule(request):
    template_name = "Schedule/schedule.html"
    print("GET", request.is_ajax())
    if request.method == "POST":
        print("POST", request.POST)
        access_token = request.user.social_auth.get().access_token
        event_body = get_event_body(request.POST["time"], request.POST["equipment"], request.POST["description"])
        # calendar_id = '1ga5hvcp7huhrh26vpa88qsf84@group.calendar.google.com'
        event = get_api_service(access_token).events().insert(calendarId='primary', body=event_body).execute()
        print('Request send seccessfully')
        print('Event created: %s' % (event.get('htmlLink')))
        return redirect(reverse("schedule"))
    return render(request, template_name)


def get_api_service(access_token):
    # credentials = service_account.Credentials.from_service_account_file(
    #     settings.GOOGLE_CALENDAR_SECRETS_FILE, scopes=settings.GOOGLE_API_SCOPES)
    service = build('calendar', 'v3', credentials=Credentials(access_token))
    return service


def get_event_body(time, equipment, description):
    calendar_id = '1ga5hvcp7huhrh26vpa88qsf84@group.calendar.google.com'
    start, end = time.split(" - ")
    start_date, start_time = start.split()
    end_date, end_time = end.split()
    print(start_date, start_time, end_date, end_time)
    event = {
        'summary': '{}'.format(equipment),
        'description': '{}'.format(description),
        'start': {
            'dateTime': '{}T{}:00'.format(start_date, start_time),
            'timeZone': 'Europe/Kiev',
        },
        'end': {
            'dateTime': '{}T{}:00'.format(end_date, end_time),
            'timeZone': 'Europe/Kiev',
        },
        'attendees': [
            {'email': calendar_id},
        ],
    }
    return event


def get_permission(request, provider):
    user_with_permission = request.user.social_auth.get(provider=provider)
    print(user_with_permission)
    return redirect(reverse("schedule"))
