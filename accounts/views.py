from django.shortcuts import render,redirect
from django.views import View
from accounts.forms import ProfileForm, SignupUserForm
from accounts.models import CustomUser
from allauth.account import views

class ProfileView(View):
    def get(self,request,*args,**kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        
        
        return render(request,'accounts/profile.html',{
            'user_data': user_data
        })
#プロフィール編集
class ProfileEditView(View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial = {
                'username':user_data.username,
                'email': user_data.email,
                'school_year':user_data.school_year,
                'school_class':user_data.school_class,
                'position':user_data.position
            }
        )
        return render(request,'accounts/profile_edit.html',{
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.username = form.cleaned_data['username']
            user_data.email = form.cleaned_data['email']
            user_data.school_year = form.cleaned_data['school_year']
            user_data.school_class = form.cleaned_data['school_class']
            user_data.positions = form.cleaned_data['position']
            user_data.save()
            return redirect('profile')
        
        return render(request, 'accounts/profile.html', {
            'form':form
        })

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'
    
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')
    
class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    form_class = SignupUserForm




        

        

    

# Create your views here.
