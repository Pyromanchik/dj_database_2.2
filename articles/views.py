from django.shortcuts import render
from .models import Article


def articles_list(request):
    template = 'articles/news.html'

    ordering = '-published_at'


    articles = Article.objects.prefetch_related(
        'scopes__tag'
    ).order_by(ordering)

    context = {
        'object_list': articles
    }

    return render(request, template, context)