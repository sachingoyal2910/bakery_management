from django.conf.urls import url
from bakery.views import AllProducts, PlaceOrder, OrderHistory

urlpatterns = [
    url(r'^products/$', AllProducts.as_view()),
    url(r'^PlaceOrder/$', PlaceOrder.as_view()),
    url(r'^OrderHistory/$', OrderHistory.as_view()),

]