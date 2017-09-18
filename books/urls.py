from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^books/$', views.publisher_list),
    url(r'^books/(?P<pk>[0-9]+)/$', views.publisher_detail),
]