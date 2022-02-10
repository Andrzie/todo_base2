from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, FormView
from todoapp.models import Task
from todoapp.forms import MyUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect



class UserRegistrationView(FormView):
    template_name = 'register.html'
    form_class = MyUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class TaskView(ListView):
    model = Task
    template_name = 'base.html'
    context_object_name = 'tasks'


class UpdateTaskView(UpdateView):
    model = Task
    fields = ['text']
    template_name = 'update_todo.html'
    success_url = '/'

class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_todo.html'
    success_url = '/'

class CreateTaskView(CreateView):
    model = Task
    template_name = 'create_todo.html'
    fields = ['text']
    success_url = '/'
