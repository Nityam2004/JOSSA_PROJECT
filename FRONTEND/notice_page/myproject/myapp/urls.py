# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_and_notices_view, name='news_and_notices'),
    # Add other URLs as needed
]
