"""cwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from travels.views import *
from travels.models import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('city', CityViewSet)
router.register('service', ServiceViewSet)
router.register('order', OrderViewSet)
router.register('company', CompanyViewSet)
router.register('favorite',  FavoriteViewSet)
router.register('comment',  CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('travels.urls')),
    path('api/', include(router.urls)),
    path('api/service-filter/', GetServiceView.as_view())
    
]
