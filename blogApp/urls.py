
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    # url(r'^$', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail,name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetail.as_view(),name='post_detail'),
    url(r'^post/new/$',views.PostCreate.as_view(), name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.PostUpdate.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostRemove.as_view(), name='post_remove'),
    url(r'^authentificate/$', views.authentificate_user, name='authentificate'),
    url(r'^logout/$', views.logout_view, name='logout'),

]


