from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from CSE_Frontend import settings

admin.autodiscover()

urlpatterns = patterns('cse.views',

    # Examples:
    # url(r'^$', 'CSE_Frontend.views.home', name='home'),
    # url(r'^CSE_Frontend/', include('CSE_Frontend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', 'home', name='home'),

    url(r'^q/$', 'q', name='q'),

    url(r'^query/(?P<key>(.*))$', 'query', name='query'),

    url(r'^snapshot/(?P<did>(.*))$', 'snapshot', name='snapshot'),

)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
