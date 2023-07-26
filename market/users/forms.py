from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1']

    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-profile-data'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-profile-data'}), required=False)
    first_name = forms.CharField(label='Firstname', widget=forms.TextInput(attrs={'class': 'form-profile-data'}), required=False)
    phone_number = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-profile-data'}), required=False)
    photo = forms.ImageField(widget=forms.FileInput, required=False)
    
    
    # def clean_avatar(self):
    #     avatar = self.cleaned_data.get('avatar')
    #     if avatar is None:
    #         raise forms.ValidationError(u'Добавьте картинку')
    #     if 'image' not in avatar.content_type:
    #         raise forms.ValidationError(u'Неверный формат картинки')
    #     return avatar
    
    
    class Meta:
        model = CustomUser
        fields = ['photo', 'username', 'first_name','email',  'phone_number']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

