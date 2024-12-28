from django.shortcuts import render, redirect
from . import models


# Create your views here.
def index(request):
    if request.method == 'POST':
        task: str = request.POST.get('task')
        if task:
            new_task = models.Todo()
            new_task.title = task
            new_task.save()
            return redirect('index')

    todos = models.Todo.objects.all()
    return render(request, 'todo/index.html', context={'todos': todos})


def delete_todo(request, todo_id: int):
    todo = models.Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')


