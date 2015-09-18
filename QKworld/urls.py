from django.conf.urls import include, url,include
from django.contrib import admin
from django.conf import settings
urlpatterns = [
    # Examples:
    # url(r'^$', 'QKworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.server',
    	{'document_root':settings.STATICTFILES_DIRS}),
]
