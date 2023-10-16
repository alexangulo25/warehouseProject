from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import warehouse 
from .resources import uploadResources
from tablib import Dataset
from .forms import ArchivoForm
import requests

# def simple_upload(request):
#     if request.method == 'POST':
#         upload_resource = uploadResources()
#         dataset = Dataset()
#         new_record = request.FILES['myfile']

#         if not new_record.name.endswith('csv'):
#             return render(request, 'warehouse_main')
        
#         imported_data = dataset.load(new_record.read(), format="csv")

#         for data in imported_data:
#             value = warehouse(
#                 data[0],
#                 data[1],
#                 data[2]
#             )

#             value.save()
#     return render(request, 'warehouse_main')
def subir_archivo(request):
    url = 'http://127.0.0.1:5000/bulk'
    
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            values = request.POST['nombre']
            print(values)
            myobj = {
            "id": 1,
            "fileName": values
            }
            x = requests.post(url, json = myobj)
            print(x)
            return redirect('warehouse_main')
    else:
        form = ArchivoForm()
    template_name = 'base/subir_archivo.html'
    return render(request, 'base/subir_archivo.html', {'form': form})
    
class Login(LoginView):
    template_name = 'base/loginTemplate.html'
    field = '__all__'
    redirect_authenticated_user =  True

    def get_success_url(self):
        return reverse_lazy('warehouse_main')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user =  True
    success_url = reverse_lazy('warehouse_main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('warehouse_main')
        return super(RegisterPage, self).get( *args, **kwargs)


class WarehouseView(LoginRequiredMixin, ListView):
    model = warehouse
    context_object_name = 'items'

class itemDetail(LoginRequiredMixin, DetailView):
    model = warehouse
    context_object_name = 'itemView'
    template_name = 'base/itemD.html'


class createRecord(LoginRequiredMixin, CreateView):
    model = warehouse
    fields = '__all__'
    success_url = reverse_lazy('warehouse_main')
    template_name = 'base/warehose_form.html'

class editRecord(LoginRequiredMixin, UpdateView):
    model = warehouse
    fields = '__all__'
    success_url = reverse_lazy('warehouse_main')
    template_name = 'base/warehose_form.html'

class deleteRecord(LoginRequiredMixin, DeleteView):
    model = warehouse
    context_object_name = 'deleteView'
    fields = '__all__'
    success_url = reverse_lazy('warehouse_main')
    template_name = 'base/deleteitem.html'