from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.CreateAccountView.as_view(), name='register'),

    path('dashboard/', views.TaskDashboard.as_view(), name='dashboard'),

    #add newtask urlpattern here

    path('updatetask/<int:pk>/', views.EditTask.as_view(), name='update-task'),
]
