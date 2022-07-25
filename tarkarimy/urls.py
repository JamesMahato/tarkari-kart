
from django.urls import path
from tarkarimy import views

urlpatterns = [
    path('',views.index, name='index'),
    path('product/', views.product, name='product'),
]

