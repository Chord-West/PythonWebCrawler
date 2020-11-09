from django.db import models
# django models의 class는 DB의 Table이 됨

class BlogData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.title