from google.auth.transport.requests import Request
import json
import requests
from datetime import datetime
from google.oauth2.id_token import verify_oauth2_token
from CalendarApp import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from oauth2client import client
# from oauth2client.client import verify_id_token


class GoogleIDTokenAuthenticationBackend(object):
    def authenticate(self, request):
        #print(request.POST)
        #id_token = json.loads(request.body)["id_token"]
        # id_token = request.POST['id_token']
        # print(id_token)
        # id_info = verify_id_token(id_token, settings.GOOGLE_CLIENT_ID)

        print(request.POST["auth_code"])

        # if not request.header.get("X-Requested-With"):
        #     return HttpResponseForbidden("This request does not have `X-Requested-With` header")

        credentials = client.credentials_from_clientsecrets_and_code(settings.GOOGLE_CLIENT_SECRETS_FILE, ["https://www.googleapis.com/auth/calendar.events", "profile", "email"], request.POST["auth_code"])

        print(credentials.access_token)

        id_info = credentials.id_token

        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return HttpResponse('Unauthorized', status=401)
        # expiry = datetime.utcfromtimestamp(id_info['exp']).strftime('%Y-%m-%d %H:%M:%S')
        # print(expiry)
        try:
            user = User.objects.get(username=id_info['name'])
            print(user, "exist")
        except User.DoesNotExist:
            user = User.objects.create_user(username=id_info['name'], email=id_info['email'],
                                            first_name=id_info['given_name'], last_name=id_info['family_name'])
            user.set_unusable_password()
            user.save()
            print(user, "not exist")
        if not user.is_active:
            return HttpResponse('User inactive or deleted.', status=401)

        # if expiry < datetime.date.today():
        #     print(expiry)
        #     raise exceptions.AuthenticationFailed(_('Token Expired.'))

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
