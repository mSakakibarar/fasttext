from django.urls import path

from . import views

urlpatterns = [
    path('category1', views.Category1.as_view(), name='category1'),
    path('category2', views.Category2.as_view(), name='category2'),
]