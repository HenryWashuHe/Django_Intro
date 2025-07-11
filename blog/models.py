from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title=models.TextField()
    brief_summary = models.TextField()
    content=models.TextField()
    published_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
