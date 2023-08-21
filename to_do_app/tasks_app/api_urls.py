from tasks_app.api_views import test_view, task_list, task_create, task_detail, task_update, task_delete
from django.urls import path

urlpatterns = [
    path('test', test_view),
    path('tasks', task_list),
    path('create', task_create),
    path('detail/<int:pk>', task_detail),
    path('update/<int:pk>', task_update),
    path('delete/<int:pk>', task_delete),
]
