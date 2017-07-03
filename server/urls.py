from django.conf.urls import url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from customer import views as customer_view
from chain import views as chain_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^customers/$', customer_view.CustomerList.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/$', customer_view.CustomerDetail.as_view()),
    url(r'^chains/$', chain_view.ChainList.as_view()),
    url(r'^chains/(?P<pk>[0-9]+)/$', chain_view.ChainDetail.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/chains/$', customer_view.CustomerChainView.as_view()),
]
