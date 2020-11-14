from django import forms

from apps.general_pages.models import ContactMe


class ContactMeModelForm(forms.ModelForm):
	class Meta:
		model = ContactMe
		fields = ('name','email','subject','message')