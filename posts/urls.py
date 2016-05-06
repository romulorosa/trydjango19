from django.conf.urls import url, include

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

urlpatterns = [
    url(r'^create/$', post_create),
    url(r'^detail/$', post_detail),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
    url(r'^$', post_list),
]
