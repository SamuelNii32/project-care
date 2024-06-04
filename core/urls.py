from django.urls import path

from core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('search/', views.search, name='search'),
]
