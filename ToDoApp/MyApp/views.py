
from MyApp.models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from MyApp.Serializers import MySerializer



@api_view(["GET"])
def MyHome(request):
    task_list = Task.objects.all()
    all_data = MySerializer(task_list, many=True)
    return  Response(all_data.data)


@api_view(["GET"])
def DeleteTask(request, TaskId):
    Onetask = Task.objects.get(id = TaskId)
    Onetask.delete()
    return Response("You Delete Task")

@api_view(["POST"])
def CreateData(request):
    print(request.data)
    serializer = MySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("You Created New Task...")



@api_view(["POST"])
def UpdateData(request, TaskId):
    Onetask = Task.objects.get(id=TaskId)
    serializer = MySerializer(instance=Onetask, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("You Updated New Task...")

















