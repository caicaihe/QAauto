from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', env_setting),
    url(r'^add/$', env_add),
    url(r'^delete/$', env_delete),
    ]
