from django import forms
from GiftIdeasForTeachers.choices import SUBJECTCHOICES
from GiftIdeasForTeachers.choices import COFFEECHOICES
from GiftIdeasForTeachers.choices import CHILDCHOICES
from GiftIdeasForTeachers.choices import SPORTSCHOICES
from GiftIdeasForTeachers.choices import HUMORCHOICES
from GiftIdeasForTeachers.models import Gift

class PriceForm(forms.Form):
	price_cap = forms.DecimalField(label='What is your spending limit?', max_digits=5, decimal_places=2, required=False)
	likes = forms.CharField(label="If you could name one thing that your teacher likes, what would it be?", max_length=100, required=False)
	subject = forms.ChoiceField(label="In what subject area does your teacher teach?", choices=SUBJECTCHOICES, required=False)
	coffee = forms.ChoiceField(label="Does your teacher drink coffee?", choices=COFFEECHOICES, widget=forms.RadioSelect)
	hasChildren = forms.ChoiceField(label="Does your teacher have children under the age of 10?", choices=CHILDCHOICES, widget=forms.RadioSelect)
	sportsFan = forms.ChoiceField(label="Does your teacher follow sports?", choices=SPORTSCHOICES, widget=forms.RadioSelect)
	hasASenseOfHumor = forms.ChoiceField(label="Does your teacher have a good sense of humor?", choices=HUMORCHOICES, widget=forms.RadioSelect, required=False)

class NewGiftForm(forms.ModelForm):
	class Meta:
		model = Gift
		fields = ['giftTitle', 'price', 'webAddress', 'comment', 'image']

