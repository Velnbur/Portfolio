from django.shortcuts import render, HttpResponse
from .models import ArticlesModel
from django.utils.html import strip_tags


def blog_view(request):
    articles = ArticlesModel.objects.all()
    top_articles = ArticlesModel.objects.order_by("-views")
    for article in articles:
        article.text = " ".join(strip_tags(article.text).split(" ")[:60])
    for article in top_articles:
        article.text = " ".join(strip_tags(article.text).split(" ")[:15]) + "..."

    context = {
        "articles": articles,
        "top_articles": top_articles,
    }
    return render(request, "blog.html", context)


def article_view(request, article_id):
    article = ArticlesModel.objects.get(id__exact=article_id)
    article.views += 1
    article.save()

    context = {"article": article}
    return render(request, "article.html", context)
