from django.shortcuts import render, HttpResponse


def home_view(request):
    """base html render func"""
    return render(request, "index.html")


def portfolio_view(request):
    return HttpResponse("Portfolio")
