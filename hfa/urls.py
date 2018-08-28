from django.conf.urls import url
from backend import views
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^errors/list/$', views.error_code_list),
    path('admin/', admin.site.urls),
]
urlpatterns = format_suffix_patterns(urlpatterns)
