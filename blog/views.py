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

def get_index_page(request):
    all_articles=Article.objects.all()
    return render(request, 'blog/index.html',{'article_list':all_articles})
def get_detail_page(request):
    curr_article=Article.objects.all()[0]
    section_list=curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
            {
                        'curr_article':curr_article,
                        'section_list':section_list
                    })