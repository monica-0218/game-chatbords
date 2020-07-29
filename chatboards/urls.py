from .views import IndexView
from django.urls import path

app_name = 'chatboards'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]