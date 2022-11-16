from django.shortcuts import render,redirect,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import context
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Favorite

from .forms import FavoriteForm

class CreateFavoriteView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwrags):
        context = {'form': FavoriteForm()}
        return render(request, 'fav/favarite_form.html', context)
    
    def post(self,request,*args,**kwargs):
        form = FavoriteForm(request.POST,request.FILES)
        if not form.is_valid():
            return render(request,'fav/favarite_form.html',{'form':form})
        
        favorite = form.save(commit=False)
        favorite.submitter = self.request.user
        #モデルオブジェクトのsave()の時に、ファイルがアップロードされる
        favorite.save()
        return render(request,'fav/favarite_list.html')
    
def list(request):
    data = Favorite.objects.all()
    params = {
        'data':data
    }
    return render(request,'fav/favarite_list.html',params)

    
    

    
    
# Create your views here.
