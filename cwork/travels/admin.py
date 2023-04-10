from django.contrib import admin
from .models import City, Service, Order, Company, Favorite, Comment
from django.db.models import QuerySet
from django.contrib.auth.models import User
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


class RatingFilter(admin.SimpleListFilter):
	title = 'Бюджет'
	parameter_name = 'price'

	def lookups(self, request, model_admin):
		return [
			('<13', 'Низкий'),
			('от 13 до 15', 'Средний'),
			('>=15', 'Высокий'),
		]

	def queryset(self, request, queryset:QuerySet):
		if self.value()=='<13':
			return queryset.filter(price__lt=13000)
		if self.value()=='от 13 до 15':
			return queryset.filter(price__gte=13000).filter(price__lt=15000)
		if self.value()=='>=15':
			return queryset.filter(price__gte=15000)
		return queryset


@admin.register(City)
class CityAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
	list_display = [ 'id', 'name', 'slug']
	list_editable = [ 'name','slug']
	prepopulated_fields = {'slug' : ('name', )}


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
	list_display = ['id', 'title', 'slug', 'offers', 'price', 'currency']
	list_editable = ['title', 'slug', 'offers', 'price']
	prepopulated_fields = {'slug' : ('title', )}
	actions = ['set_rubles']
	list_filter= [RatingFilter]

	@admin.action(description = 'Установить валюту в рубли')
	def set_rubles(self, request, qs:QuerySet):
		count_updated = qs.update(currency=Service.RUB)
		self.message_user(request,f'Было обновлено {count_updated} записей')

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
	list_display = ['id', 'service','name', 'number']


@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
	list_display = ['name', 'id']

@admin.register(Favorite)
class FavoriteAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
	list_display = ['service', 'id']

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
	list_display = ['user', 'text']






admin.site.site_header = 'Админка тур-компании'
admin.site.index_title = 'Тур-компания: Вокруг света'