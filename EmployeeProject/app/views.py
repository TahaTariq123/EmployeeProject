from datetime import datetime
from django.views.generic import TemplateView
from app.models import Employee
from django.urls import reverse_lazy
from EmployeeServices.forms import EmployeeForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render

class HomeView(TemplateView):
    """Renders the home page."""
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        """Adds additional context data to the template."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Employee Management System'
        context['year'] = datetime.now().year
        employee_data = Employee.objects.all()
        final_data = employee_data.values()
        print(final_data)
        context['final_data'] = final_data
        return context
        

class ContactView(TemplateView):
    """Renders the contact page."""
    template_name = 'app/contact.html'

    def get_context_data(self, **kwargs):
        """Adds additional context data to the template."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        context['message'] = 'Important Contact Details'
        context['year'] = datetime.now().year
        context['phone'] = '8882792771'
        return context

class AboutView(TemplateView):
    """Renders the about page."""
    template_name = 'app/about.html'

    def get_context_data(self, **kwargs):
        """Adds additional context data to the template."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        context['message'] = 'Your application description page.'
        context['year'] = datetime.now().year
        return context
