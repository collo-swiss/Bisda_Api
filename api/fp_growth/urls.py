from django.conf.urls import url

from api.fp_growth.views import *

app_name = 'projects'

urlpatterns = [
    url(r'^', cluster, name='cluster'),
]
