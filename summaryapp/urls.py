from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # home() 함수가 루트 URL에서 실행
]
