from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.API_test),
    #url(r'API/$', views.API_test),
    #url(r'registry/$',views.registry_test),
    url(r'exec/$',views.exec),

]
