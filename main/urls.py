# main/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_before_login, name='index_before_login'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('class-schedule/', views.class_schedule, name='class_schedule'),
    path('study-repository/', views.study_repository, name='study_repository'),
    path('time-and-study-methods/', views.time_and_study_methods, name='time_and_study_methods'),
    path('goal-tracking/', views.goal_tracking, name='goal_tracking'),
]
