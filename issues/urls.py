from django.conf.urls import patterns, include, url
from issues.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',url(r'^home', home),
    # Examples:
    # url(r'^$', 'issues.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
