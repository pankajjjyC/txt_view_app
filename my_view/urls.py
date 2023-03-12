from django.urls import path
from . import views

urlpatterns = [    
    # path('login',views.login,name='login'),
    path('',views.index,name='index'),   
    path('read_file',views.read_file,name='read_file'), 
  
]