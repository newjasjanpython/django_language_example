from django.urls import path
from .views import *


urlpatterns = [
    path('', index_page),
    path('language-change/', change_language_view),
]

