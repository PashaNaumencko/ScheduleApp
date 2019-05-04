from .views import schedule, projects, auth
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('auth/', include('social_django.urls', namespace='social')),
    path("logout", LogoutView.as_view(), name="logout"),
    path("tokensignin", auth.auth, name="token-signin"),
    path("schedule", schedule.schedule, name="schedule"),
    path("projects/current", projects.current_projects, name="current"),
    path("projects/my", projects.my_projects, name="my"),
    path("projects/<int:project_id>", projects.my_projects, name="project-info"),
    path("projects/requests", projects.requests, name="requests"),
    path("projects/requests/<int:request_id>", projects.my_projects, name="request-info"),
    # path("auth/complete/<str:provider>", schedule.get_permission, name="get-permission"),
]
