import requests
import re
from datetime import datetime
from . import models
from bs4 import BeautifulSoup
from django.contrib.auth.models import User

PAGES = 10


def get_article_urls():
    urls = []
    for i in range(1, PAGES + 1):
        r = requests.get("https://habr.com/en/page{}/".format(i))
        html = BeautifulSoup(r.text, "html.parser")
        urls += [a.get("href") for a in html.find_all("a", "post__title_link")]
    return urls


def save_data(urls: list):
    for url in urls:
        r = requests.get(url)
        html = BeautifulSoup(r.text, "html.parser")
        models.ArticlesModel.objects.create(
            heading=html.find("span", "post__title-text").string,
            text=html.find(id="post-content-body").string,
            author=User.objects.get(username__exact="Velnbur"),
        )


def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def main():
    urls = get_article_urls()


if __name__ == "__main__":
    main()
