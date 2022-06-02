from django.urls import path
from articles import views

app_name ='articles' #다른 앱들과 중복 방지하기위해 이름명시
urlpatterns = [
    path('index/', views.index),
    path('dinner/<str:name>/', views.dinner),
    path('review/', views.review),
    path('create_review/', views.create_review, name='create_review'),
]
