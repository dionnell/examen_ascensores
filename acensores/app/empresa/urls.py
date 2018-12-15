from django.conf.urls import include, url
from app.empresa.views import empresa_view, empresa_list


urlpatterns = [
     url(r'^$', empresa_view, name='empresa_view'),
     url(r'^lista$', empresa_list, name='lista'),
]
