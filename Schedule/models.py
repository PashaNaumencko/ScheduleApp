from django.contrib.auth.models import User
from django.db import models


class Request(models.Model):
    initiator = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    # document = models.FileField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    document = models.FileField(blank=True)
    # admin = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class UserInProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.user, self.project)
