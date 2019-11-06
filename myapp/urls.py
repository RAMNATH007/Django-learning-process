from django.urls import path
from .import views
urlpatterns = [
    path('live/', views.hello, name="hello"),
    path('live1/', views.hello1, name='hello1')
]