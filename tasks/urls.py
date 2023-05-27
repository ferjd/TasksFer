from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('tasks/update_status/<int:task_id>/', views.update_status, name='update_status'),
    path('update_importance/<int:task_id>/', views.update_importance, name='update_importance'),
    path('update_urgency/<int:task_id>/', views.update_urgency, name='update_urgency'),
    path('update_observations/<int:task_id>/', views.update_observations, name='update_observations'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
