from django import forms
from allauth.account.forms import SignupForm

class ProfileForm(forms.Form):    
    email = forms.EmailField(label='Email')
    username = forms.CharField(max_length=30,label='姓')
    school_year = forms.IntegerField(label='学年')
    school_class = forms.IntegerField(label='クラス')
    position = forms.CharField(label='ポジション',max_length=30)
    
class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


    
    
    