from django.shortcuts import render
from .models import Article
# Create your views here.
def home(request):
     articls = Article.objects.filter(status=True)
     return render(request, 'blog_app/home.html', context={'articls': articls})