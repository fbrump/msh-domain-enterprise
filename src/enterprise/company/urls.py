from django.conf.urls import url
from company.views import company_list, company_detail

urlpatterns = [
    url(r'^companies/$', company_list),
    url(r'^companies/(?P<code>)$', company_detail),
]