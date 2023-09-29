from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registerLead/', views.registerLead, name="registerLead")
]