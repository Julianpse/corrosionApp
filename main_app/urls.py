from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^tech$', views.tech, name = 'tech'),
    url(r'^create_equipment$', views.create_equipment),
    url(r'^view_data$', views.view_data)
]
