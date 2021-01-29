from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from blog.models import Article
from blog.schemas import ArticleSchema, ArticleResponseSchema


@csrf_exempt  # testing purposes; you should always pass your CSRF token with your POST requests (+ authentication)
@require_http_methods("POST")
def create_article(request):
    try:
        # fetch the user and pass it to schema
        import json
        json_data = json.loads(request.body)
        author = User.objects.get(id=json_data['author'])
        schema = ArticleSchema.create(
            author=author,
            title=json_data['title'],
            content=json_data['content']
        )
        return JsonResponse({
            'article': schema.dict()
        })
    except User.DoesNotExist:
        return JsonResponse({'detail': 'Cannot find a user with this id.'}, status=404)


def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        schema = ArticleSchema.from_django(article)
        return JsonResponse({
            'article': schema.dict()
        })
    except Article.DoesNotExist:
        return JsonResponse({'detail': 'Cannot find an article with this id.'}, status=404)


def get_all_articles(request):
    articles = Article.objects.all()
    data = []

    for article in articles:
        schema = ArticleResponseSchema.from_django(article)
        data.append(schema.dict())

    return JsonResponse({
        'articles': data
    })
