from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^agenda/', views.agenda, name='agenda'),
    url(r'^keynote_speakers', views.keynote_speakers, name='keynote_speakers'),
    url(r'^opening_remarks', views.opening_remarks, name='opening_remarks'),
    url(r'ie', views.ie, name='ie'),
    url(r'sustainability', views.sustainability, name='sustainability'),
    url(r'competition', views.competition, name='competition'),
    url(r'collaborators', views.collaborators, name='collaborators'),
    url(r'start_up', views.start_up, name='start_up'),
    url(r'finance', views.finance, name='finance'),
    url(r'^panelist/', views.panelist, name='panelist'),
    url(r'high_tech', views.high_tech, name='high_tech'),
    url(r'^feature_events', views.feature_events, name='feature_events'),
    url(r'job_fair', views.job_fair, name='job_fair'),
    url(r'register_job', views.register_job, name='register_job'),
    url(r'career', views.career, name='career'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^about_us', views.about_us, name='about_us'),
    url(r'^test', views.test, name='test')
]