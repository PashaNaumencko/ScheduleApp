from .views import schedule, projects, auth, about
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("schedule", schedule.schedule, name="schedule"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("tokensignin", auth.auth, name="token-signin"),
    path("projects/my", projects.my_projects, name="my"),
    path("projects/current", projects.current_projects, name="current"),
    path("projects/requests", projects.requests, name="requests"),
    path("about", about.about, name="about"),
    path('auth/', include('social_django.urls', namespace='social')),
    # path("auth/complete/<str:provider>", schedule.get_permission, name="get-permission"),
]
