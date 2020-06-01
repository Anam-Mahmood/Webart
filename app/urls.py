from django.urls import path
from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.conf.urls.static import static
from django.urls import include
from . import views
from . import admin
from .views import Home, Inspo, InspoLoginView, Index, LoginView, health
from django.conf import settings

urlpatterns = [
               # path('', views.index, name='index'),
               path('health', views.health, name='health'),
               # path('404', views.handler404, name='404'),
               # path('500', views.handler500, name='500'),
               url(r'^$', Index.as_view(), name='index'),
               path('', include('django.contrib.auth.urls')),
                # url(r'^login/$', login, {'authentication_form': LoginForm}, name='login'),
               url(r'^signup-or-login/(?P<signup>[0-1]+)/$', LoginView.as_view(), name='login'),
                # url(r'^logout/$', logout, {'next_page': 'index'}, name='logout'),
               url(r'^home/$', Home.as_view(), name='home'),
               url(r'^inspo/$', Inspo.as_view(), name='inspo'),
               url(r'^inspo_login/$', InspoLoginView.as_view(), name='inspo_login'),
]
