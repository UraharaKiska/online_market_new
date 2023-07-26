from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, LoginUserForm, UpdateUserForm
from .models import CustomUser

class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    # success_url = reverse_lazy('login')
    template_name = 'users/register.html'
    #
    # def post(self, request, *args, **kwargs):
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.save()

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile_update(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(username=request.user)
        user_form = UpdateUserForm(request.POST, request.FILES, instance=user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            # print(user_form.username)
            return redirect('lk')

    else:
        user_form = UpdateUserForm(instance=request.user)

    context = {
        'user_form': user_form,
    }

    return render(request, 'users/personal-page.html', context)
