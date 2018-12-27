from django.conf.urls import url
from apps.run_APItest.views import *


urlpatterns = [
    url(r'^$', exec),
    #url(r'API/$', views.API_test),
    #url(r'registry/$',views.registry_test),
    url(r'exec/$', exec),

]
