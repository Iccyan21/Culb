from django.urls import path
from fav import views

urlpatterns = [
    path('form/',views.CreateFavoriteView.as_view(), name='form'),
    path('list/',views.list, name='list')
]
