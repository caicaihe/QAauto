from django.conf.urls import url
from apps.run_UItest.views import *


urlpatterns = [
    url(r'^$', UI_test),
    #url(r'API/$', views.API_test),
    #url(r'registry/$',views.registry_test),
    url(r'exec/$', exec),

]