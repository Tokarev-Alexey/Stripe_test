from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('item/<int:id>/', views.item, name='item'),
    path('buy/<int:id>/', views.buy, name='buy')
]
