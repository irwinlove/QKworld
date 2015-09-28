from django.conf.urls import include, url,include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'QKworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'blog.views.register',name='register'),
    url(r'^login/$', 'blog.views.user_login',name='login'),
    url(r'^logout/$', 'blog.views.user_logout',name='logout'),
    url(r'^restricted/$', 'blog.views.restricted',name='restricted'),
	] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
# 	# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 	urlpatterns += [
#         url(r'^static/(?P<path>.*)$', serve,{
#             'document_root':settings.STATIC_ROOT,
#             }),
#     ]