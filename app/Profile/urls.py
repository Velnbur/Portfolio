from django.urls import path
from . import views

urlpatterns = [
    path("<slug>", views.profile_view, name="profile"),
    path("log_out/", views.log_out, name="log_out"),
]
