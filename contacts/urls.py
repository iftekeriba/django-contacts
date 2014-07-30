from django.conf.urls import patterns, url
from contacts import views

urlpatterns = patterns('',
    url(r'^$', views.ContactListView.as_view(), name='list'),
    url(r'^create/$', views.ContactCreateView.as_view(), name='create'),
)
