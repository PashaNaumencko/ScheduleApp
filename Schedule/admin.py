from django.contrib import admin
from .models import Project, UserInProject, Request

# Register your models here.

admin.site.register(Project)
admin.site.register(UserInProject)
admin.site.register(Request)
