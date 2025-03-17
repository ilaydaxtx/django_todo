from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from .models import Task

class taskList(ListView):
    """ template = loader.get_template('firstTemplate.html') """
    """ return HttpResponse(template.render()) """
    model = Task
    template_name = "task_list.html"

# Create your views here.
