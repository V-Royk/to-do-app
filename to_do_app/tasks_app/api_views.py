from django.http import HttpRequest
from django.http.response import JsonResponse, HttpResponseBadRequest
from tasks_app.models import Task
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import  get_object_or_404
from django.db import IntegrityError 
from django.http.response import HttpResponseNotFound

import json


@csrf_exempt
def handle_tasks(request: HttpRequest) -> JsonResponse|HttpResponseBadRequest:
    match request.method:
        case "GET":
            return task_list(request)
        case "POST":
            return task_create(request)
        

@csrf_exempt
def handle_task(
    request: HttpRequest,
    pk: int
) -> JsonResponse|HttpResponseBadRequest:
    match request.method:
        case "GET":
            return task_detail(request, pk)
        case "PUT":
            return task_update(request, pk)
        case "PATCH":
            return done_task(request, pk)
        case "DELETE":
            return task_delete(request, pk)


def task_list(request: HttpRequest) -> JsonResponse|HttpResponseBadRequest:
    if request.method == "GET":
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
    
    return HttpResponseBadRequest(content={
        "error": "invalid method",
    })


@csrf_exempt
def task_create(request: HttpRequest) -> JsonResponse|HttpResponseBadRequest:
    if request.method == "POST":
        if len(request.body) == 0:
            return HttpResponseBadRequest(content="Error: Empty body")

        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest(content="Invalid JSON")

        title = body.get("title")
        if not title:
            return HttpResponseBadRequest(content="No title")

        description = body.get("description")
        Task.objects.create(title=title, description=description)
        return JsonResponse(data={
            "success": True
        })

    return HttpResponseBadRequest(content={
        "error": "invalid method",
    })


def task_detail(
    request: HttpRequest, 
    pk: int
) -> JsonResponse|HttpResponseBadRequest:
    if (request.method == "GET"):

        try:
            task = Task.objects.filter(id=pk)[0]
        except IndexError:
            return HttpResponseNotFound()

        # task = get_object_or_404(Task, pk=pk)
        return JsonResponse(data={
            "title": task.title,
            "is_done": task.is_done,
            "done_date": task.done_date,
            "create_at": task.create_at,
            "update_at": task.update_at,
            "description": task.description,
        })
    
    return HttpResponseBadRequest(content={
        "error": "invalid method",
    })

@csrf_exempt
def task_update(
    request: HttpRequest, 
    pk: int
) -> JsonResponse|HttpResponseBadRequest:
    if request.method == 'PUT':
        task = get_object_or_404(Task, pk=pk)

        if len(request.body) == 0:
            return HttpResponseBadRequest(content="Error: Empty body")
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest(content="Invalid JSON")
        
        task.title = data.get('title', task.title)
        task.is_done = data.get('is_done', task.is_done)
        task.description = data.get('description', task.description)
        task.save()
        return JsonResponse({"message": "Обновлена задача"})
    
    return HttpResponseBadRequest()


@csrf_exempt
def task_delete(
    request: HttpRequest, 
    pk: int
) -> JsonResponse|HttpResponseBadRequest:
    if request.method == 'DELETE':
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return JsonResponse({"message": "Задача удалена"})
    else:
        return HttpResponseBadRequest()

def done_task(
    request: HttpRequest, 
    pk: int
) -> JsonResponse|HttpResponseBadRequest:
    """
    1. Запрос клиента
    2. Парсинг json (превращение строки в словарь)
    3. Проставляем значение из json
    4. Возвращаем ответ
    """

    if request.method == "PATCH":
        task = get_object_or_404(Task, pk=pk)
        data = json.loads(request.body)
        task.is_done = data.get('is_done', task.is_done)
        task.save()
        return JsonResponse({'success': True})
    else:
        return HttpResponseBadRequest()

        



        
        
        



    

