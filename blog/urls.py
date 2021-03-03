from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('account/',views.account, name='account'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]