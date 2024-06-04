from django.urls import path

from hirings import views


urlpatterns = [
    path('', views.hire_writer, name='hire-writer'),
]
