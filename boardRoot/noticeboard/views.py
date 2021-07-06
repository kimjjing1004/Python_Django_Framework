from django.shortcuts import render
from noticeboard.models import Notice
# Create your views here.

def index(request):
    article_list = Notice.objects.all().order_by('-writeDate')
    context = {'article_list': article_list}
    return render(request, 'noticeboard/index.html', context)



def write_article(request):
    return render(request, 'noticeboard/writeArticle.html')