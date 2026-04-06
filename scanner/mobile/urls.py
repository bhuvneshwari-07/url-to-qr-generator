from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_page, name='input_page'),
    path('result/<int:qr_id>/', views.result_page, name='result'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/<int:qr_id>/', views.delete_qr, name='delete_qr'),
]

#  {% comment %} project name - scanner, app name -  mobile , environment name - env {% endcomment %}