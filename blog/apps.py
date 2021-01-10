from django.apps import AppConfig

from blog.models import Article


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        # Create the Article table
        Article.create_table()
