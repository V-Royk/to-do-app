from django.http.response import JsonResponse, HttpResponseBadRequest
from tasks_app.models import Task
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import  get_object_or_404

import json

"""
2xx - успешный запрос
3xx - редирект
4хх - ошибка со стороны клиента
5хх - ошибка на стороне сервера
"""


def test_view(request):
    response_content = {
        "data": [
            {
                "success" : 200,
                "method": "test",
                "content": "None"
            }
        ]
    }
    return JsonResponse(data=response_content)

def task_list(request):
    tasks = Task.objects.all()
    new_list = []
    for task in tasks:
        new_task = {
            "title": task.title,
            "is_done": task.is_done,
            "done_date": task.done_date,
            "create_at": task.create_at,
            "update_at": task.update_at,
            "description": task.description,
        }
        new_list.append(new_task)
    return JsonResponse(data={'tasks': new_list})


@csrf_exempt
def task_create(request):
    body = json.loads(request.body)
    title = body.get("title")
    description = body.get("description")
    task = Task.objects.create(title=title, description=description)

    return JsonResponse(data={
        "success": True
    })

    # return JsonResponse(data={
    #     "title": task.title,
    #     "is_done": task.is_done,
    #     "done_date": task.done_date,
    #     "create_at": task.create_at,
    #     "update_at": task.update_at,
    #     "description": task.description,
    # })

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return JsonResponse(data={
        "title": task.title,
        "is_done": task.is_done,
        "done_date": task.done_date,
        "create_at": task.create_at,
        "update_at": task.update_at,
        "description": task.description,
    })

@csrf_exempt
def task_update(request, pk):
    if request.method == 'PUT':
        task = get_object_or_404(Task, pk=pk)
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.is_done = data.get('is_done', task.is_done)
        task.description = data.get('description', task.description)
        task.save()
        return JsonResponse({"message": "Обновлена задача"})
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def task_delete(request, pk):
    if request.method == 'DELETE':
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return JsonResponse({"message": "Задача удалена"})
    else:
        return HttpResponseBadRequest()

    

