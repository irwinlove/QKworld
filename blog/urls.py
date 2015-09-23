from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'QKworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'blog.views.blog_list',name='blog_list'),
    url(r'detail/(?P<blog_id>[\w\-]+)$', 'blog.views.blog_detail',name='blog_detail'),
]


