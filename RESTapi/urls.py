from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/companies/(?P<pk>[0-9]+)$',
        views.get_delete_update_company,
        name='get_delete_update_company'
    ),
    url(
        r'^api/v1/companies/$',
        views.get_post_companies,
        name='get_post_companies'
    )
]