from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from blog.models import Article
from blog.schemas import ArticleSchema


@csrf_exempt  # testing purposes, you should always pass your CSRF token with your POST requests (+ authentication)
@require_http_methods("POST")
def create_article(request):
    try:
        # fetch the user and pass it to schema
        author = User.objects.get(id=request.POST['author'])
        schema = ArticleSchema.create(
            author=author,
            title=request.POST['title'],
            content=request.POST['content']
        )
        return JsonResponse({
            'article': schema.dict()
        })
    except User.DoesNotExist:
        return JsonResponse({'detail': 'Cannot find an user with this id.'}, status=404)


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
        schema = ArticleSchema.from_django(article)
        data.append(schema.dict())

    return JsonResponse({
        'articles': data
    })
