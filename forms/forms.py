from django import forms
from django.forms import ModelForm
from . models import VehicleData


#create form

choices_list = ['Two wheeler', 'Three wheeler', 'Four wheeler']

class VechicleForm(forms.ModelForm):
	class Meta:
		model = VehicleData
		fields = ('Vehicle_Number', 'Vehicle_Type', 'Vehicle_Model', 'Description')
		widgets = {
			'Vehicle_Number' : forms.TextInput(attrs={'class': 'form-control'}),
			'Vehicle_Type' : forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
			'Vehicle_Model' : forms.TextInput(attrs={'class': 'form-control'}),
			'Description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Minimum 50 characters required'}),



			}


class EditForm(forms.ModelForm):

	class Meta:
		model = VehicleData
		fields = ('Vehicle_Number', 'Vehicle_Type', 'Vehicle_Model', 'Description')
		widgets = {
			'Vehicle_Number' : forms.TextInput(attrs={'class': 'form-control'}),
			'Vehicle_Type' : forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
			'Vehicle_Model' : forms.TextInput(attrs={'class': 'form-control'}),
			'Description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Minimum 50 characters required'}),

		}	



