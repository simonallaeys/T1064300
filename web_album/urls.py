from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#add new views here
from album.views import main_page
from users.views import logout_page, register_page
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete, password_change, password_change_done

urlpatterns = patterns('',
	
    # Examples:
    # url(r'^$', 'web_album.views.home', name='home'),
    # url(r'^web_album/', include('web_album.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
	#index
	(u'^$', main_page),
	
	#login
	(r'^login/$', login),
    
    #logout
	(r'^logout/$', logout_page),
	
    #password_reset
	(r'^password_reset/$', password_reset),

    #password_reset_done
	(r'^password_reset_done/$', password_reset_done),

    #password_reset_confirm
	(r'^password_reset_confirm/$', password_reset_confirm),

    #password_reset_complete
	(r'^password_reset_complete/$', password_reset_complete),

    #password_change
	(r'^password_change/$', password_change),

    #password_change_done
	(r'^password_change_done/$', password_change_done),
	
	#register
	(r'^register/$', register_page),

)
