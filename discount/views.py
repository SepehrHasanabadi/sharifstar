from django.shortcuts import render
from django.views.generic import FormView

class Discount(FormView):
    template_name = 'discount/index.html'
    
