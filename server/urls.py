from django.conf.urls import url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from chain import views as chain_view
from coupon import views as coupon_view
from customer import views as customer_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^customers/$', customer_view.CustomerList.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/$', customer_view.CustomerDetail.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/chains/$', customer_view.CustomerChainView.as_view()),
    # Add a view for CustomerChainDetail similar to Coupon detail
    url(r'^chains/$', chain_view.ChainList.as_view()),
    url(r'^chains/(?P<pk>[0-9]+)/$', chain_view.ChainDetail.as_view()),
    url(r'^chains/(?P<pk>[0-9]+)/coupons/$', coupon_view.CouponList.as_view()),
    url(r'^chains/(?P<pk_chain>[0-9]+)/coupons/(?P<pk_coupon>[0-9]+)/$', coupon_view.CouponDetail.as_view()),
]