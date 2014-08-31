from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from contacts import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hostco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
)
