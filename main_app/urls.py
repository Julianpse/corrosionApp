from django.conf.urls import url, include
from main_app import views


urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^tech$', views.tech, name = 'tech'),
    url(r'^create_equipment$', views.create_equipment),
    url(r'^view_data$', views.view_data)
]
