from django import forms
from django.db.models import fields
from .models import Users

class UserForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = '__all__'