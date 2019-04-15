from django.contrib.auth.models import User
from django.db import models
# from oauth2client.contrib.django_util.models import CredentialsField


# class GoogleCredential(models.Model):
#     """
#     Model for saving Google credentials to a persistent database (cf. https://developers.google.com/api-client-library/python/auth/web-app)                         # noqa: E501
#     The user ID is used as the primary key, following https://github.com/google/google-api-python-client/blob/master/samples/django_sample/plus/models.pyself.    # noqa: E501
#     (Note that we don't use oauth2client CredentialsField as that library is deprecated).
#     """
#     user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
#     token = models.CharField(max_length=255, null=True)
#     refresh_token = models.CharField(max_length=255, null=True)
#     token_uri = models.CharField(max_length=255, null=True)
#     client_id = models.CharField(max_length=255, null=True)
#     client_secret = models.CharField(max_length=255, null=True)
#     scopes = models.CharField(max_length=255, null=True)
#
#     def update_from_credentials(self, credentials):
#         """
#         Update the user credentials' from a google.oauth2.credentials.Credentials object
#         """
#         self.token = credentials.token
#         if credentials.refresh_token is not None:
#             # The refresh token is only provided on the first authorization from the user
#             # (cf. https://stackoverflow.com/questions/10827920/not-receiving-google-oauth-refresh-token)
#             # To troubleshoot a RefreshError, try visiting https://myaccount.google.com/permissions,
#             # removing the Cleo app access, and adding it again by visiting the 'authorize' view
#             self.refresh_token = credentials.refresh_token
#         self.token_uri = credentials.token_uri
#         self.client_id = credentials.client_id
#         self.client_secret = credentials.client_secret
#         self.scopes = credentials.scopes
#         self.save()
