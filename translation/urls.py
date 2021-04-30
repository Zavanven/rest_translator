from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from translation import views

urlpatterns = [
    path('translations/', views.TranslationList.as_view()),
    path('translation/<int:pk>/', views.TranslationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)