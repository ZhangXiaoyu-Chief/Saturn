from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^publishers/$', views.publisher_list),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.publisher_detail),
]