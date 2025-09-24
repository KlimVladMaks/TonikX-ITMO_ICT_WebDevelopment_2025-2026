from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Owner, Car


def root_redirect(request):
    return redirect('owners_list')


def owners_list(request):
    """
    Представление для отображения списка всех владельцев автомобилей.
    """
    owners = Owner.objects.all()
    return render(request, 'owners/owners_list.html', {'owners': owners})


def owner_detail(request, id):
    """
    Представление для отображения детальной информации об автовладельце.
    """
    try:
        owner = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        raise Http404("Автовладелец не найден")
    
    return render(request, 'owners/owner_detail.html', {'owner': owner})


class CarsListView(ListView):
    model = Car
    template_name = 'cars/cars_list.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'
