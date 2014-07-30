from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^contacts/', include('contacts.urls', namespace='contacts',
        app_name='contacts')),

    url(r'^admin/', include(admin.site.urls)),
)
