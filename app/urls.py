from django.urls import path
from app import views

urlpatterns = [
    #path('', views.BaseView.as_view(), name='index'),
    path('',views.list, name='list')
]