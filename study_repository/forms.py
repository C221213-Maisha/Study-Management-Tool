from django import forms
from .models import File, Folder

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']
