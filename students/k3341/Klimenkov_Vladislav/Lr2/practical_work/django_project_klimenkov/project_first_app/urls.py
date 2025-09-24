from django.urls import path
from . import views


urlpatterns = [
    path('', views.root_redirect),

    # Владельцы
    path('owner/list/', views.owners_list, name='owners_list'),
    path('owner/<int:id>/', views.owner_detail, name='owner_detail'),

    # Автомобили
    path('car/list/', views.CarsListView.as_view(), name='cars_list'),
    path('car/<int:car_id>/', views.CarDetailView.as_view(), name='car_detail'),
]
