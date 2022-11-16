from django.shortcuts import render
from django.views.generic import TemplateView
from fav.models import Favorite

def list(request):
    data = Favorite.objects.all()
    params = {
        'data':data
    }
    return render(request,'fav/favarite_list.html',params)




# Create your views here.
