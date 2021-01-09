from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from blog.commands import CreateArticleCommand
from blog.queries import ListArticlesQuery, GetArticleByIDQuery


@csrf_exempt  # testing purposes, you should always pass your CSRF token with your requests
@require_http_methods(["POST"])
def create_article(request):
    cmd = CreateArticleCommand(
        author=request.POST['author'],
        title=request.POST['title'],
        content=request.POST['content']
    )
    return JsonResponse(cmd.execute().dict())


def get_article(request, article_id):
    query = GetArticleByIDQuery(id=article_id)
    record = query.execute()
    return JsonResponse(record.dict(), safe=False)


def get_article_list(request):
    query = ListArticlesQuery()
    records = [record.dict() for record in query.execute()]
    return JsonResponse(records, safe=False)


