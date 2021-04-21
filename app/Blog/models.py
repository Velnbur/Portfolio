from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class ArticlesModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50, verbose_name="Heading", default="")
    text = RichTextField()
    date = models.DateTimeField(auto_now=True, verbose_name="Date")
    views = models.IntegerField(default=0)
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Icon",
        default="../img/test-photo.jpg",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.heading
