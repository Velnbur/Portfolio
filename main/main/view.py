""" import django render function for basic rendering """
from django.shortcuts import render


def home_view(request):
    """base html render func"""
    return render(request, "index.html")
