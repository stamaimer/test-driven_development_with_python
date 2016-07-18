from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lists.views.index', name='index'),
    url(r"^lists/", include("lists.urls")),
    # url(r'^admin/', include(admin.site.urls)),
)
