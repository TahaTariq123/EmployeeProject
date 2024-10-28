from django.shortcuts import render
from app.models import Employee
from django.urls import reverse_lazy
from .forms import EmployeeForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render

# Create your views here.

class EmployeeCreateView(CreateView):
    """View for creating a new employee."""
    model = Employee
    form_class = EmployeeForm
    template_name = 'app/employee_form.html'
    success_url = reverse_lazy('employee-create-success')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Task'] = "Create"
        return context

def employee_create_success_view(request):
    """Render the employee creation success page."""
    return render(request, 'app/success.html')

class EmployeeUpdateView(UpdateView):
    """View for updating an existing employee."""
    model = Employee
    form_class = EmployeeForm
    template_name = 'app/employee_form.html'
    success_url = reverse_lazy('employee-update-success') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Task'] = "Update"
        return context

class EmployeeDeleteView(DeleteView):
    """View for deleting an existing employee."""
    model = Employee
    template_name = 'app/employee_confirm_delete.html'
    success_url = reverse_lazy('home') 

def employee_update_success_view(request):
    """Render the employee update success page."""
    return render(request, 'app/success.html')
