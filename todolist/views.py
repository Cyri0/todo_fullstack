
from rest_framework.decorators import api_view

from .serializers import TaskSerializer
from .models import Task

from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST'])
def taskHandler(request):
    if request.method == 'GET':
        # adja vissza a taskokat
        tasks = Task.objects.filter(is_visible = True)
        serialized = TaskSerializer(tasks, many = True)
        return Response(serialized.data)

    if request.method == 'POST':
        # hozzon létre új taskot
        text = request.data['text']
        task = Task(text=text)
        task.save()
        serialized = TaskSerializer(task, many=False)
        return Response(serialized.data)
    
@csrf_exempt
@api_view(['PUT', 'DELETE'])
def specificTaskHandler(request, pk):
    try:
        task = Task.objects.get(id = pk)
    except:
        return Response({'message':'Task not found!'})

    if request.method == 'DELETE':
        task.is_visible = False
        task.save()
        return Response({'message':f'Task ID {pk} is removed successfully!'})
    
    if request.method == 'PUT':
        try:
            task.text = request.data['text']
            task.is_visible = request.data['is_done']
            task.is_done = request.data['is_visible']
            task.save()
            serialized = TaskSerializer(task, many=False)
            return Response(serialized.data)
        except Exception as e:
            return Response({'error':repr(e)})

