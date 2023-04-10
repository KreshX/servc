from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login),
    path('main/', views.main),
    path('offers/<slug:slug_city_offers>', views.city_offers, name='city_offers-detail'),
    path('offer/<slug:slug_tour>', views.tour, name='tour-detail'),
    path('list_order/', views.list_order),
    path('done/', views.done),
    path('change/<int:pk>/update', views.NewsUpdateView.as_view(), name='order-update' )
]