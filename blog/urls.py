from django.urls import path

from blog import views

urlpatterns = [
    path('test/', views.test_view),
]