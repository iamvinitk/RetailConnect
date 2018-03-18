from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^signup/$', views.signup),
    url(r'^login/$', views.obtain_auth_token),

]
