from django.urls import path
from .views import login_view, logout_view, home_view, about_us_view, form_view, services_view, signup_view, dashboard_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('', home_view, name='home'),
    path('about/', about_us_view, name='about_us'),
    path('contact/', form_view, name='form_view'),
    path('services/', services_view, name='services'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
