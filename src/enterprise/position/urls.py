# enterprise/position/urls.py
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^v1/positions/$', views.get_post_position, name='get_post_position'),
    url(r'^v1/positions/(?P<code>[0-9-a-z-A-Z]+)/$', views.get_delete_update_postion, name='get_delete_update_postion'),
]

urlpatterns = format_suffix_patterns(urlpatterns)