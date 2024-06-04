from django.urls import path

from contacts import views


urlpatterns = [
    path('', views.contact_us, name='contact-us'),
]
