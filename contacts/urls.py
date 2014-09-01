__author__ = 'jakal'

from django.conf.urls import patterns, url

from contacts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_person/$', views.add_person, name='add_person'),
    url(r'^person/(?P<person_name_url>\w+)/$', views.person, name='person'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
)