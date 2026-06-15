from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # assigning a post list view to the root url
    path('post/<int:pk>/', views.post_detail, name='post_detail'),   
]