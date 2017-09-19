from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^publishers/$', views.publisher_list),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.publisher_detail),
    url(r'^authors/$', views.AuthorList.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view()),
    url(r'^books/$', views.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
]