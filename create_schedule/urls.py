from django.urls import path
from . import views

urlpatterns = [
    path('class-schedule/', views.class_schedule, name='class-schedule'),
    path('see-schedule/', views.see_schedule, name='see-schedule'),
]
