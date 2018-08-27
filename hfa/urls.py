from django.conf.urls import url, include
from rest_framework import routers
from backend import views
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'errors', views.ErrorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
