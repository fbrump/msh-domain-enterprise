# enterprise/position/urls.py
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    #url(r'^positions/$', company_list),
    #url(r'^positions/(?P<code>[0-9-a-z-A-Z]+)/$', company_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)