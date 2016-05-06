from django.conf.urls import url, include

urlpatterns = [
    url(r'^create/$', "posts.views.post_create"),
    url(r'^detail/$', "posts.views.post_detail"),
    url(r'^update/$', "posts.views.post_update"),
    url(r'^delete/$', "posts.views.post_delete"),
    url(r'^$', "posts.views.post_list"),
]
