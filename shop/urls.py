from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shop import views

urlpatterns = [
    path('shops/', views.ShopList.as_view()),
    path('shops/<int:pk>/', views.ShopDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
