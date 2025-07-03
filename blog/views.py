from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
import csv
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
def get_detail_page(request, article_id):
    curr_article=None
    all_articles=Article.objects.all()
    previous_index=0
    next_index=0
    for index, article in enumerate(all_articles):
        if index==0:
            previous_index=0
            next_index=index+1
        elif index==len(all_articles)-1:
            next_index=index
            previous_index=index-1
        else:
            previous_index=index-1
            next_index=index+1

        if article.article_id == article_id:
            curr_article=article
            previous_article=all_articles[previous_index]
            next_article=all_articles[next_index]
            break
    section_list=curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
            {
                        'curr_article':curr_article,
                        'section_list':section_list,
                'previous_article':previous_article,
                'next_article':next_article,
                    })
def get_csv_page(request):
    rows=[]
    if request.method=='POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        decoded_file=csv_file.read().decode('utf-8').splitlines()
        reader=csv.reader(decoded_file)
        rows=list(reader)
        print("CSV_Data",rows)

    return render(request, "blog/csv_test.html", {'rows':rows})
