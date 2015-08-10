"""TalkDoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from dajaxice.core import dajaxice_autodiscover
from django.shortcuts import redirect
dajaxice_autodiscover()

from login.views import signup, socialAuth, user_approval


urlpatterns = patterns('',
    url(r'^$', redirect, {'url': '/welcome/'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^welcome/', 'login.views.welcome_page'),
    url(r'^login/', 'login.views.log_in'),
    url(r'^logout/', 'login.views.log_out'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^talkdoc/', include('TalkDoc.urls')),
    url(r'^approval/(?P<id>[-\w]+)/$', user_approval, name='user_approval'),
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

    # URL for Social Auth
    url(r'^socialAuth/$', socialAuth, name='socialAuth'),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
    )

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

    url(r'^adminmedia/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT + '/admin', 'show_indexes': True}),


)





