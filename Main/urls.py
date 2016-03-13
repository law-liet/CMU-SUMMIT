from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^panelist/', views.panelist, name='panelist'),
    url(r'^feature_events', views.feature_events, name='feature_events')
]