from django.conf.urls import patterns, include, url
from .views import cliente
from .views import padmin
from .views import login
from django.contrib.auth import logout
from .views import index

urlpatterns = patterns('',
   
    url(r'^$', index.as_view()),
    url(r'^cliente/$', cliente.as_view(), name = 'cliente'),
    url(r'^PANEL/$', padmin.as_view(), name = 'padmin'),

    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name':'inicio/login.html'},name = 'login'),

    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',name = 'logout'),
)

