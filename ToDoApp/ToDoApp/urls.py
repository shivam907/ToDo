
from django.contrib import admin
from django.urls import path
from MyApp.views import MyHome, DeleteTask, CreateData, UpdateData


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", MyHome),
    path("delete_task/<int:TaskId>/", DeleteTask),
    path("update_task/<int:TaskId>/", UpdateData),
    path("create_task/", CreateData),
    ]


