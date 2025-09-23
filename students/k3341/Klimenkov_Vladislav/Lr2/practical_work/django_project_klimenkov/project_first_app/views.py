from django.shortcuts import render
from django.http import Http404
from .models import Owner


def owner_detail(request, id):
    """
    Представление для отображения детальной информации об автовладельце.
    """
    try:
        owner = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        raise Http404("Автовладелец не найден")
    
    return render(request, 'owners/owner_detail.html', {'owner': owner})
