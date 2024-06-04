from django.urls import path

from projects import views


urlpatterns = [
    path('<str:department>/topics', views.projects, name='projects'),
    path('<str:department>/<str:topic>/', views.project, name='project'),
    path('payment/<str:department>/<str:topic>/<str:firstName>/<str:lastName>/<str:email>/<str:phone>/<str:amount>/<str:selected>/<str:referrer>/<str:reference>/', view=views.payment, name='payment'),
    path('refresh-content/', views.refresh_content, name='refresh'),
]

