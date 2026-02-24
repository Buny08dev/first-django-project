from django.shortcuts import render
from django.views.generic import FormView,ListView,View,DetailView,TemplateView,DeleteView,UpdateView
# Create your views here.

class OrderView(TemplateView):
    template_name='order.html'