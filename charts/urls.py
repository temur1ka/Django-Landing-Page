from django.urls import path
from .views import ClubView, get_contact, registerPage, loginPage, logOutPage

urlpatterns = [
    path('', ClubView.as_view(), name='index'),
    path('main/', get_contact, name='contact'),
    
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logOutPage, name='logout'),



]