from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CustomUserCreationForm, LoginUserForm, UpdateUserForm
from .models import CustomUser
from basket.cart import Cart
from basket.views import basket_add_session
import copy

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
        # cart = Cart(request).copy
        # login(self.request, user)
        return redirect('login')


# def reister(request):
#     if request.method == 'POST':
#         user_form = CustomUserCreationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)


def logout_user(request):
    logout(request)
    return redirect('login')



def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            # print(cd['password'])
            # print(cd['p'])


            if user is not None:
                cart = Cart(request)
                session_cart = []
                cart.clear()
                # for c in cart:
                #     print(c)
                # print(session_cart)
                
                login(request, user)
                basket_add_session(request, cart)
                return redirect('home')
            else: 
                # messages.error(request, 'IDI NA HUI')
                # print('HUUUUUUUUUI')
                return render(request, 'users/login.html', {'form': form})

    else:
        form = LoginUserForm()
        return render(request, 'users/login.html', {'form': form})






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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password-reset.html'
    email_template_name = 'users/password-reset-email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')