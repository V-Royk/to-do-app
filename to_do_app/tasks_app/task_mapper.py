from tasks_app.models import Task
from django.utils.timezone import now


class TaskNotExistError(Exception):
    def __init__(self, id: int):
        self.id = id

        
    def __str__(self):
        return f'task with id{self.id} does not exist'


class TaskMapper:
    def __init__(self, model: Task):
        self.model = model

    
    def get_all_task(self):
        return self.model.objects.all()

    
    def get_task_by_id(self, pk: int) -> Task:
        try:
            task = self.model.objects.filter(id=pk)[0]
            return task
        except IndexError:
             raise TaskNotExistError(pk)


    def task_create(self, title: str, description: str) -> Task:
        task = self.model.objects.create(title = title, description = description)
        return task


    def task_update(self, pk: int, title: str, description: str) -> bool:
        task = self.get_task_by_id(pk)
        task.title = title
        task.description = description
        task.update_at = now()
        task.save()
        return True


    def task_delete(self, pk: int) -> bool:
        task = self.get_task_by_id(pk)
        task.delete()
        

              
       






task_mapper = TaskMapper(Task)





    

