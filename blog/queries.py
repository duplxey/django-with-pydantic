from typing import List

from pydantic import BaseModel

from blog.models import Article


class ListArticlesQuery(BaseModel):

    def execute(self) -> List[Article]:
        articles = Article.list()

        return articles


class GetArticleByIDQuery(BaseModel):
    id: str

    def execute(self) -> Article:
        article = Article.get_by_id(self.id)

        return article
