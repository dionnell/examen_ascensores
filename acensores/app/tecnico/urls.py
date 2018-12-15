from django.conf.urls import include, url
from app.tecnico.views import index 
from .views import registro
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

urlpatterns = [
     url(r'^$', index, name='index'),
     url(r'^registrate$', registro.as_view(), name='registrate'),
     url(r'^login$',  LoginView.as_view(template_name='iniciosesion.html'), name='login'),
    # url(r'^user_login$',user_login,name='user_login'),

]
