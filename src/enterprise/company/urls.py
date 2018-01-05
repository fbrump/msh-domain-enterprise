from django.conf.urls import url
from company.views import company_list

urlpatterns = [
    url(r'^companies/$', company_list),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]