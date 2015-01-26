from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
     url(r'^$', include('games.urls')),
     url(r'^games/', include('games.urls')),
    url(r'^admin/', include(admin.site.urls)),
     # user auth urls

    url(r'^login/$',  'games.views.login'),
    url(r'^auth/$',  'games.views.auth_view'),    
    url(r'^logout/$', 'games.views.logout'),
    url(r'^loggedin/$', 'games.views.loggedin'),
    url(r'^invalid/$', 'games.views.invalid_login'),    
    url(r'^invalid_update_login/$', 'games.views.invalid_update_login'),   
    url(r'^register/$', 'games.views.register_view'),
    url(r'^register_success/$', 'games.views.register_success'),


    url(r'^update_login/$',  'games.views.update_login'),    

    url(r'^update/$',  'games.views.update_view'),  
	url(r'^update_start/$',  'games.views.update_start'),  
    url(r'^add_start/$',  'games.views.add_start'),  
    url(r'^add_login/$',  'games.views.add_login'),   
    url(r'^add_register/$',  'games.views.add_register'),  
    url(r'^add_game/$',  'games.views.add_game'),  
    url(r'^update_game/$',  'games.views.update_game'), 
    url(r'^about/$',  'games.views.about'), 

    url(r'^test_editable/$', 'games.views.test_editable'),
    
    #Table view
    #url(r'^people/$',  'games.views.people'),

)


