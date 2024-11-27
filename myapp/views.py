from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from myapp.models import BlogPost

class BlogView(ListView):
    model=BlogPost#=BlogPost.objects.all()
    context_object_name='posts'#posts à utiliser dans les pages html
    template_name="blogView.html"
    
class blogcreate(CreateView):
    model = BlogPost
    fields=['title','content','author','created_on']# soit fields soit form class
    #form_class=blogform formulaire dans forms.py
    template_name = "blogcreate.html"
    success_url=reverse_lazy('Posts:listhtml')

