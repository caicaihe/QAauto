from django.conf.urls import url, include

from . import view

 
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^run_test/', view.run_test),

    url(r'^env_setting/', include("env_setting.urls")),
    url(r'^run_APItest/', include("run_APItest.urls")),
    url(r'^run_UItest/', include("run_UItest.urls")),
]