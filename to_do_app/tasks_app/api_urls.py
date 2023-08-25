from tasks_app.api_views import handle_task, handle_tasks
from django.urls import path

# tasks/ - GET получние списка задач
# tasks/create - GET получение формы для создания задачи
# tasks/id/update - GET получение формы для обновления задчи
# tasks/id - GET деталка задачи
# tasks/ - POST cоздание задач
# tasks/id - DELETE удаление задачи
# tasks/id - PUT обновление задачи

urlpatterns = [
    path('tasks', handle_tasks),
    path('tasks/<int:pk>', handle_task),
]
