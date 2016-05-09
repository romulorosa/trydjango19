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
    url(r'^(?P<post_id>\d+)/detail/$', post_detail, name="detail"),
    url(r'^(?P<post_id>\d+)/edit/$', post_update, name="edit"),
    url(r'^(?P<post_id>\d+)/delete/$', post_delete),
    url(r'^$', post_list, name="list"),
]
