from django.urls import path

from blog import views

urlpatterns = [
    path('create-article/', views.create_article),
    path('article/<str:article_id>/', views.get_article),
    path('article-list/', views.get_article_list),
]