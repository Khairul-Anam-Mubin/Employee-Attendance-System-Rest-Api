from django.urls import path
from django.urls.resolvers import URLPattern 
from account import views

urlpatterns = [
    path('createAccount',views.createAccountApi), 
    path('showEmployee',views.showEmployeeApi),  
    path('showEmployee/<int:pk>',views.showEmployeeApi),  
]