from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'QKworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'blog.views.blog_list',name='blog_list'),
]


