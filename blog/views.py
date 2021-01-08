from django.http import HttpResponse, JsonResponse

from blog.commands import CreateArticleCommand
from blog.models import Article


def get_by_id_view(request, article_id):
    return JsonResponse(Article.get_by_id(article_id).json(), safe=False)


def get_by_title_view(request, article_title):
    return JsonResponse(Article.get_by_title(article_title).json(), safe=False)


def test_view(request):
    print("test_view")

    cmd = CreateArticleCommand(
        author='john@doe.com',
        title='New Article',
        content='Super awesome article'
    )

    article = cmd.execute()
    db_article = Article.get_by_id(article.id)

    print(article.json())

    return HttpResponse(db_article.title)

