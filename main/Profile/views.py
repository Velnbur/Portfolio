from django.shortcuts import render, HttpResponse


def profile_view(request):
    return HttpResponse("<h1>Profile</h1>")


def log_out(request):
    return HttpResponse("Log out")
