from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")

def article_content (request):
    article=Article.objects.all()[0]
    title=article.title
    brief_summary=article.brief_summary
    content=article.content
    article_id=article.article_id
    published_date=article.published_date
    return_str='title: %s, brief_summary: %s, content:%s, article_id:%s, published_date:%s' %(title,brief_summary,content,article_id,published_date)
    return HttpResponse(return_str)