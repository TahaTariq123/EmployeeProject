"""
Definition of urls for EmployeeProject.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms
from app.views import *
from EmployeeServices.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('employee/create/success/', employee_create_success_view, name='employee-create-success'),
    path('employee/update/success/', employee_update_success_view, name='employee-update-success'),
]
