from django.urls import path

from blog import views

urlpatterns = [
    path('articles/create/', views.create_article),
    path('articles/<str:article_id>/', views.get_article),
    path('articles/', views.get_all_articles),
]
