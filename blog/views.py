from django.http import JsonResponse

from blog.models import Article
from blog.schemas import ArticleSchema


def create_article(request):
    pass


def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        schema = ArticleSchema.from_django(article)
        return JsonResponse({
            'article': schema.dict()
        })
    except Article.DoesNotExist:
        return JsonResponse({'detail': 'Cannot find an article with this id.'}, status=404)


def get_article_list(request):
    articles = Article.objects.all()
    data = []

    for article in articles:
        data.append(ArticleSchema.from_django(article).dict())

    return JsonResponse({
        'articles': data
    })
