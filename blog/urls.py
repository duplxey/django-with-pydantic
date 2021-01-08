from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path('id/<str:article_id>/', views.get_by_id_view),
    path('title/<str:article_title>/', views.get_by_title_view),
    path('test/', views.test_view),
]