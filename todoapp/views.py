from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def addTask(request):
    print(f"Authenticated User: {request.user}, Is Authenticated: {request.user.is_authenticated}")

    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(owner=request.user)
    print(request.user)
    return Response(serializer.data)


@api_view(['PUT'])
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response('Item successfully deleted!')