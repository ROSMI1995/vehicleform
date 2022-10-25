from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,CreateView, UpdateView
from. models import VehicleData
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from .forms import EditForm, VechicleForm
from django.urls import reverse



def delete(request, id):
  post = VehicleData.objects.get(id=id)
  post.delete()
  return HttpResponseRedirect(reverse('home'))





class EditDataView(UpdateView):
	model = VehicleData
	form_class = EditForm
	template_name = 'edit_data.html'
	#fields = ['Vehicle_Number', 'Vehicle_Type', 'Vehicle_Model', 'Description']
	success_url = reverse_lazy('home')


    

class RegisterView(generic.CreateView):
	form_class = VechicleForm
	template_name = 'Vechicleform.html'
	success_url = reverse_lazy('home')



class HomePageView(ListView):
	model = VehicleData
	template_name = 'index.html'
	context_object_name = 'all_data_list'


	