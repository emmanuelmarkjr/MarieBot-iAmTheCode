from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^send/danger/alert/(?P<address>.+)$', views.danger_alert, name='danger_alert'),
    url(r'^results/$', views.ajax_user_search, name='demo_user_search')
]