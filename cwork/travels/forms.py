from django import forms

class OrderForm(forms.Form):
	name = forms.CharField(label='Имя')
	number = forms.CharField(label='Номер телефона')

	# name = forms.CharField(label='Имя')
	# surname = forms.CharField(label='Фамилия')
	# feedback = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows':2, 'cols':20}))
	# rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=10)