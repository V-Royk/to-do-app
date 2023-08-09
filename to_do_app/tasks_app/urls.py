from django.contrib import admin
from django.urls import path

from tasks_app.views import *


# REST

# CRUD - create read update delete

# tasks/ - GET получние списка задач
# tasks/create - GET получение формы для создания задачи
# tasks/id/update - GET получение формы для обновления задчи
# tasks/id - GET деталка задачи
# tasks/ - POST cоздание задач
# tasks/id - DELETE удаление задачи
# tasks/id - PUT обновление задачи

urlpatterns = [
     path('tasks/', handle),
     path('tasks/<int:pk>', handle_task),
     path('tasks/create', get_create_form),  
     path('tasks/<int:pk>/update', get_update_form),
     path('tasks/<int:pk>/delete', task_delete),  
]
