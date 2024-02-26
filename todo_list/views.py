from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# All Tasks


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

# Detail View


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo_list/task.html'
