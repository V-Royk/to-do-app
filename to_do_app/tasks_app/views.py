from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.utils.timezone import now
from django.http.response import HttpResponse, HttpResponseNotFound
from django.http.request import HttpRequest
from tasks_app.task_mapper import task_mapper, TaskNotExistError



from pprint import pprint


def task_list(request):
    tasks = task_mapper.get_all_task()
    return render(request, 'task_list.html', {'task_list': tasks})



# def task_detail(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     return render(request, 'task_detail.html', {'task': task})
def task_detail(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        task = task_mapper.get_task_by_id(pk)
        return render(request, 'task_detail.html', {'task': task})
    except TaskNotExistError:
        return HttpResponseNotFound()



def task_create(request):
    pprint(request.POST)
    title = request.POST['titleKey']
    description = request.POST['descriptionKey']
    task = task_mapper.task_create(title, description)
    return redirect(f"http://127.0.0.1:8000/tasks/{task.id}")



def task_update(request, pk):
    title = request.POST['titleKey']
    description = request.POST['descriptionKey']
    try:
        task_mapper.task_update(pk, title, description)
    except TaskNotExistError:
        return HttpResponseNotFound()
    return redirect(f"http://127.0.0.1:8000/tasks/{pk}")



def task_delete(request, pk):
    task_mapper.task_delete(pk)
    return redirect(f"http://127.0.0.1:8000/tasks")

# tasks/
# GET - получить список задач
# POST - создать задчу

def handle(request):
    if request.method == 'POST':
        return  task_create(request)
    if request.method == 'GET':
        return task_list(request)



def handle_task(request, pk):
    if request.method == 'DELETE':
        return  task_delete(request, pk)
    if request.method == 'POST':
        return task_update(request, pk)
    if request.method == 'GET':
        return task_detail(request, pk)



def get_update_form(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_update.html', {'task': task})



def get_create_form(request):
    return render(request, 'create_form.html', {})



def get_update_form(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'update_form.html', {'task': task})









 









