from django.conf.urls import url
from apps.env_setting.views import *

urlpatterns = [
    url(r'^$', base),
    url(r'^setting/$', env_setting),
    url(r'^add/$', env_add),
    url(r'^delete/$', env_delete),
    url(r'^set_auto/$', env_auto),
    url(r'^add_auto/$', envauto_add),
    url(r'^delete_auto/$', envauto_delete),
    url(r'^set_manual/$', env_manual),
    url(r'^add_auto/$', envmanual_add),
    ]
