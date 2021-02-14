from django.conf.urls import url
from users.views import RegisterCustomerView, login_request
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^signup/$', RegisterCustomerView.as_view()),
    url(r'^login/$',login_request, name="login"),
]