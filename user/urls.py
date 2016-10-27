from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.UserList.as_view(),
        name='user_list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user_detail'),
    url(r'^create/$',
        views.UserCreate.as_view(),
        name='user_create'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        views.UserUpdate.as_view(),
        name='user_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.UserDelete.as_view(),
        name='user_delete'),
]