from django.shortcuts import render, HttpResponse

# Create your views here.
def blog_view(request):
    return render(request, "blog.html")


def article_view(request, article_id):
    return HttpResponse("{}".format(article_id))
