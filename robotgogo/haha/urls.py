from django.conf.urls import url, include

from haha.view import *

 
urlpatterns = [
    url(r'^$', hello),
    url(r'^run_test/', include("run_test.urls")),
    url(r'^webhook/', webhook),

    url(r'^env_setting/', include("env_setting.urls")),
    url(r'^run_APItest/', include("run_APItest.urls")),
    url(r'^run_UItest/', include("run_UItest.urls")),
]