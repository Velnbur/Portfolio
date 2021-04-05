from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_view, name="blog"),
    path("<slug>", views.article_view, name="article"),
]
