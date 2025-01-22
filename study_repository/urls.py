from django.urls import path
from . import views

app_name = 'study_repository'

urlpatterns = [
    path('', views.study_repository, name='home'),
    path('<int:folder_id>/', views.study_repository, name='home'),
    path('create-folder/<int:parent_id>/', views.create_folder, name='create_folder'),
    path('upload-file/<int:parent_id>/', views.upload_file, name='upload_file'),
    path('edit-folder/<int:folder_id>/', views.edit_folder, name='edit_folder'),
    path('delete-folder/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
]
