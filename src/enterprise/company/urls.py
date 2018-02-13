from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from company.views import company_list, company_detail

urlpatterns = [
    url(r'^companies/$', company_list),
    url(r'^companies/(?P<code>[0-9-a-z-A-Z]+)/$', company_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)