from rest_framework import serializers
from .models import *

class CitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = City
        fields = ['url', 'name', 'slug']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Service
        fields = ['url','title', 'slug', 'offers', 'price', 'currency']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['url', 'service','name','number']


class CompanySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields = ['url', 'name']


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Favorite
        fields = ['url', 'service']


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ['url', 'user', 'text']
