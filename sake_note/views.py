from django.shortcuts import render
from .models import Sake
from .forms import SakeForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView



class IndexView(ListView):
    model=Sake
    template_name="sake_note/index.html"
    context_object_name="sake_list"
    ordering=["-created_at"]

class SakeCreateView(CreateView):
    model=Sake
    form_class=SakeForm
    template_name="sake_note/sake_form.html"
    success_url=reverse_lazy("index")

class SakeUpdateView(UpdateView):
    model=Sake
    form_class=SakeForm
    template_name="sake_note/sake_form.html"
    success_url=reverse_lazy("index")

class SakeDeleteView(DeleteView):
    model=Sake
    template_name="sake_note/sake_confirm_delete.html"
    success_url=reverse_lazy("index")

