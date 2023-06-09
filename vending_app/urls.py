from django.urls import path
from . import views

app_name = 'vending_app'

urlpatterns = [
    path('', views.sandwiches, name='sandwiches'),
    path('salads/', views.salads, name='salads'),
    path('snacks/', views.snacks, name='snacks'),
    path('drinks/', views.drinks, name='drinks'),
    path('sweets/', views.sweets, name='sweets'),
]


