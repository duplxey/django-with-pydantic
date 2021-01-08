from django.http import HttpResponse

from blog.commands import CreateArticleCommand
from blog.models import Article


def test_view(request):
    print("test_view")

    cmd = CreateArticleCommand(
        author='john@doe.com',
        title='New Article',
        content='Super awesome article'
    )

    article = cmd.execute()
    db_article = Article.get_by_id(article.id)

    return HttpResponse(db_article.title)

