from django.urls import path
from .views import BlogView, blogcreate

urlpatterns = [
path('liste',BlogView.as_view(),name='listhtml'),
path('create',blogcreate.as_view(),name='createhtml'),

]