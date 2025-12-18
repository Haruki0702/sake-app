from django.shortcuts import render
from .models import Sake
from .forms import SakeForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class IndexView(ListView):
    model=Sake
    template_name="sake_note/index.html"
    context_object_name="sake_list"
    ordering=["-created_at"]

class SakeCreateView(LoginRequiredMixin, CreateView):
    model=Sake
    form_class=SakeForm
    template_name="sake_note/sake_form.html"
    success_url=reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)    

class SakeUpdateView(LoginRequiredMixin, UpdateView):
    model=Sake
    form_class=SakeForm
    template_name="sake_note/sake_form.html"
    success_url=reverse_lazy("index")

    def test_func(self):
        obj=self.get_object()
        return obj.user==self.request.user

class SakeDeleteView(LoginRequiredMixin, DeleteView):
    model=Sake
    template_name="sake_note/sake_confirm_delete.html"
    success_url=reverse_lazy("index")

    def test_func(self):
        obj=self.get_object()
        return obj.user==self.request.user

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


