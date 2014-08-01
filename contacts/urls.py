from django.conf.urls import patterns, url
from contacts import views

urlpatterns = patterns('',
    url(r'^$', views.ContactListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.ContactDetailView.as_view(), name='detail'),
    url(r'^create/$', views.ContactCreateView.as_view(), name='create'),
)
