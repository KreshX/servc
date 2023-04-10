from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_number(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s Номер не может быть отрицательным'),
            params={'value': value})

def validate_price(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s Цена не может быть отрицательной'),
            params={'value': value})
    

class Offer(models.Model):

	title = models.CharField(max_length=40)
	slug = models.SlugField(default='', null=False, blank=True)
	history = HistoricalRecords()

	# def get_url(self):
	# 	return reverse('city_offers-detail', args=[self.slug])

	def __str__(self):
		return f'{self.title}'



class City(models.Model):

	name = models.CharField(max_length=40)
	slug = models.SlugField(default='', null=False, blank=True)
	history = HistoricalRecords()
	# offers = models.ForeignKey(Offer, on_delete=models.PROTECT, null=True, blank=True)
	def get_url(self):
		return reverse('city_offers-detail', args=[self.slug])

	def __str__(self):
		return f'{self.name}'


class Service(models.Model):

	EUR = 'EUR'
	USD = 'USD'
	RUB = 'RUB'

	CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]



	title = models.CharField(max_length=40)
	slug = models.SlugField(default='', null=False, blank=True)
	offers = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
	price = models.IntegerField(default='10325', validators=[validate_price])
	currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB')
	history = HistoricalRecords()
	def get_url(self):
		return reverse('tour-detail', args=[self.slug])

	def __str__(self):
		return f'{self.title}'


class Order(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=40)
	number = models.CharField(max_length=40, validators=[validate_number])
	history = HistoricalRecords()
	def __str__(self):
		return f'{self.service}'

	def get_url(self):
		return reverse('order-update', args=[self.slug])



class Company(models.Model):
	name = models.CharField(max_length=40)
	history = HistoricalRecords()
	def __str__(self):
		return f'{self.name}'

class Comment(models.Model):
	user = models.CharField(max_length=40)
	text = models.CharField(max_length=250)
	history = HistoricalRecords()
	def __str__(self):
		return f'{self.user}'


class Favorite(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
	history = HistoricalRecords()
	def __str__(self):
		return f'{self.service}'