from MyApp.models import Task
from rest_framework.serializers import ModelSerializer

class MySerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


