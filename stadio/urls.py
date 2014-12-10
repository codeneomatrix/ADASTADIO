from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stadio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

    url(r'^', include('apps.inicio.urls')),

    url(r'^partidos/', include('apps.partidos.urls')),

	url(r'^control/', include('apps.controlzonas.urls')),  

	url(r'^controlp/', include('apps.controlpersonal.urls')),

	url(r'^controla/', include('apps.controlaficionados.urls')), 

    url(r'^venta/', include('apps.taquilla.urls')),   

)
