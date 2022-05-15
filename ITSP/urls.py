
from django import views
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,name="index"),
    path('API',views.Team_API , name="TeamApi"),
    path('API/<str:pk>',views.Team_API , name="TeamApi"),
    path('<str:pk>', views.go , name="go"),
]