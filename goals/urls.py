from django.urls import path
from . import views

urlpatterns = [
    path('goal_list/', views.goal_list, name='goal_list'),
    path('create/', views.create_goal, name='create_goal'),
    path('toggle/<int:pk>/', views.toggle_goal, name='toggle_goal'),
    path('delete/<int:goal_id>/', views.delete_goal, name='delete_goal'),
]
