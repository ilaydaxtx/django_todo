from django.urls import path
from . import views
from.views import taskList

urlpatterns = [
    path('', taskList.as_view(), name='tasks')
]