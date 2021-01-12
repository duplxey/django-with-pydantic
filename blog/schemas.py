from pydantic_django import ModelSchema

from blog.models import Article


class ArticleSchema(ModelSchema):
    class Config:
        model = Article
