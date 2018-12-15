from django.conf.urls import include, url
from app.servicio.views import servicio_view, servicio_list


urlpatterns = [
     url(r'^$', servicio_view, name='servicio_view'),
     url(r'^lista$', servicio_list, name='servicio_list'),

]