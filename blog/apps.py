from django.apps import AppConfig

from blog.models import Article


class BlogConfig(AppConfig):
    name = 'blog'

    # Create the Article table
    Article.create_table()
