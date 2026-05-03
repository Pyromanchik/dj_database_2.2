from django.shortcuts import render
from .models import Article


def articles_list(request):
    template = 'articles/news.html'

    # используйте этот параметр для упорядочивания результатов
    ordering = '-published_at'

    # Получаем все статьи с предзагрузкой связанных тегов через Scope,
    # чтобы избежать N+1 запросов и обеспечить нужную сортировку
    articles = Article.objects.prefetch_related(
        'scopes__tag'
    ).order_by(ordering)

    context = {
        'object_list': articles  # Именно так ожидается в шаблоне (object_list)
    }

    return render(request, template, context)