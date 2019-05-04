from django.contrib.auth.models import User
from django.db import models


# class Participant(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_admin = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user.username


class Request(models.Model):
    admin = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name="+")
    admin = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="+")

    def __str__(self):
        return self.title


# class UserInProject(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     project = models.ForeignKey(Project, on_delete=models.PROTECT)
#     is_admin = models.BooleanField(default=False)
#
#     def __str__(self):
#         return "{} - {}".format(self.user, self.project)
