from django.urls import path

from . import views

urlpatterns = [
    path('category1/<str:text>', views.Category1.as_view(), name='category1'),
    path('category2/<str:text>', views.Category2.as_view(), name='category2'),
]