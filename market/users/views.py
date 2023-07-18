from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

class SignUpForm(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    #
    # def post(self, request, *args, **kwargs):
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.save()

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('home')

