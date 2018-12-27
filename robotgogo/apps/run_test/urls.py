from django.conf.urls import url
from apps.run_test.views import *


urlpatterns = [
    url(r'^$', run_test),
    url(r'exec/$', exec),

]
