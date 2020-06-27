from django.db import models

from blog.models import Post

STATUS = (
    (0, "draft"),
    (1, "review"),
    (2, "published")
)


class Page(models.Model):
    topic = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.topic


class Stat(models.Model):
    pageViews = models.IntegerField(default=0)
    page = models.OneToOneField(Page, on_delete=models.CASCADE)

