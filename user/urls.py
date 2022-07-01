from django.urls import path, re_path as url
from . import views

urlpatterns = [
    path('', views.main, name="Home"),
    url(r'^id/(?P<userid>\d+)/$', views.get_user_by_id, name="IDQuery"),
    url(r'^name/(?P<username>\w{0,50})/$', views.get_user_by_name, name="NameQuery"),
]