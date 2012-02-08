from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#add new views here
from album.views import index
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
	
    # Examples:
    # url(r'^$', 'web_album.views.home', name='home'),
    # url(r'^web_album/', include('web_album.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
	#index
	(u'^$', index),
	
	#login
    (r'^accounts/login/$',  login),
    
    #logout
    (r'^accounts/logout/$', logout),
)
