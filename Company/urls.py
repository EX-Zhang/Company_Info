
from django.urls import path

from . import views

urlpatterns = [

    path("", views.Company, name='Company'),

    path("requestData/", views.getCompanyData, name='getCompanyData'),

    path('requestDetail/', views.getCompanyDetail, name='getCompanyDetail'),

    path('<str:Symbol>/', views.Detail, name='Detail'),

]
