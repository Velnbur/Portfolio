from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_view, name="blog"),
    path("article/<int:article_id>", views.article_view, name="article"),
]
