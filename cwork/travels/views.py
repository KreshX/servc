from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from django.http import HttpResponseRedirect
from .forms import OrderForm
from django.views.generic import UpdateView
from django.db.models import F, Sum, Min, Max,Count, Avg
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
import django_filters.rest_framework


def main(request):
	cities = City.objects.all()

	return render(request, 'travels/main.html' , {'cities': cities})


def city_offers(request, slug_city_offers:str):
	city_offers = get_object_or_404(City, slug=slug_city_offers)
	services = Service.objects.filter(offers=city_offers.id)
	agg = services.aggregate(Avg('price'), Max('price'), Min('price'))
	return render(request, 'travels/city_offers.html', {'city_offers': city_offers, 'agg':agg, 'services': services})

def tour(request, slug_tour:str):
	service = get_object_or_404(Service, slug=slug_tour)
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			# a = get_object_or_404(Service, slug=slug_tour)
			feed = Order( service = get_object_or_404(Service, slug=slug_tour),
				name=form.cleaned_data['name'],
				number=form.cleaned_data['number'],
				)
			feed.save()
			return HttpResponseRedirect('/done')
	else:
		form = OrderForm()
	return render(request, 'travels/tour.html', context={'form': form, 'service': service})
	# return render(request, 'travels/tour.html', {'service': service})

def login(request):
	# if request.method == 'POST':
	# 	form = OrderForm(request.POST)
	# 	if form.is_valid():
	# 		print(form.cleaned_data)
	# 		feed = Order(service=Service.objects.all()[0],
	# 			name=form.cleaned_data['name'],
	# 			number=form.cleaned_data['number'],
	# 			)
	# 		feed.save()
	# 		return HttpResponseRedirect('admin')
	# else:
	# 	form = OrderForm()
	return render(request, 'travels/login.html')
	# return render(request, 'travels/login.html')	


def list_order(request):
	orders = Order.objects.all()
	return render(request, 'travels/list_order.html' , {'orders': orders, 'total': orders.count()})

def done(request):
	return render(request, 'travels/done.html')

class NewsUpdateView(UpdateView):
	model = Order
	template_name = 'travels/update.html'
	fields = ['number']


class ServicePagination(PageNumberPagination):
    page_size = 5
    page_sizer_query_param = 'paginate_by'
    max_page_size = 10
    

class OrderPagination(PageNumberPagination):
    page_size = 4
    page_sizer_query_param = 'paginate_by'
    max_page_size = 10


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name', 'slug']
    ordering_fields = ['name', 'slug']
    filterset_fields = ['name', 'slug']


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = ServicePagination
    filter_backends = [OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    ordering_fields = ['price', 'currency']
    filterset_fields = ['title', 'slug', 'offers', 'price', 'currency']


class GetServiceView(ListAPIView):
    queryset = Service.objects.filter(Q(price__gte='12714') & Q(price__lte='89325'))
    serializer_class = ServiceSerializer
    pagination_class = ServicePagination
    filter_backends = [OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    ordering_fields = ['price', 'currency']
    filterset_fields = ['title', 'slug', 'offers', 'price', 'currency']


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    ordering_fields = ['number']
    search_fields = ['name']
    filterset_fields = ['service','name', 'number']
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def del_order(self,request, pk=None):
        order=self.queryset.get(id=pk)
        order.delete()
        return Response('Заказ был удален')
    @action(methods=['GET'], detail=False, url_path='get')
    def get_data(self, request, **kwargs):
        Orders = Order.objects.all()
        return Response({'Orders': [Order.name for Order in Orders]})


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['name']
    filterset_fields = ['name']
    

class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['user', 'text']
    ordering_fields = ['user', 'text']
    filterset_fields = ['user', 'text']	
    	