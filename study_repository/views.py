from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Folder, File
from .forms import FolderForm, FileUploadForm

@login_required
def study_repository(request, folder_id=None):
    current_folder = None
    if folder_id:
        current_folder = get_object_or_404(Folder, id=folder_id, owner=request.user)
        folders = current_folder.subfolders.all()
        files = current_folder.files.all()
    else:
        folders = Folder.objects.filter(parent=None, owner=request.user)
        files = File.objects.filter(folder__isnull=True, owner=request.user)

    folder_form = FolderForm()
    file_form = FileUploadForm()

    return render(request, 'study_repository/home.html', {
        'folders': folders,
        'files': files,
        'current_folder': current_folder,
        'folder_form': folder_form,
        'file_form': file_form,
        'folder_id': folder_id
    })

@login_required
def create_folder(request, parent_id):
    parent_folder = Folder.objects.filter(id=parent_id).first() if parent_id != 0 else None
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.parent = parent_folder
            folder.owner = request.user
            folder.save()
            return redirect('study_repository:home', folder_id=parent_id)
    return redirect('study_repository:home', folder_id=parent_id)


@login_required
def upload_file(request, parent_id=None):
    if parent_id == 0:
        parent_folder = None  # Root or no parent folder
    else:
        parent_folder = Folder.objects.filter(id=parent_id).first()

    if not parent_folder and parent_id is not None:
        return redirect('study_repository:home')

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.folder = parent_folder
            file.owner = request.user
            file.save()
            return redirect('study_repository:home', folder_id=parent_id)

    return redirect('study_repository:home', folder_id=parent_id)


@login_required
def edit_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, owner=request.user)

    if request.method == "POST":
        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            # Redirect to the appropriate location
            if folder.parent:
                return redirect(reverse('study_repository:home', kwargs={'folder_id': folder.parent.id}))
            else:
                return redirect(reverse('study_repository:home'))  # Redirect to the root if no parent
    else:
        form = FolderForm(instance=folder)

    return render(request, 'study_repository/edit_folder.html', {'form': form, 'folder': folder})

@login_required
def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, owner=request.user)

    if request.method == "POST":
        # Perform the deletion on POST request
        parent_folder_id = folder.parent.id if folder.parent else None
        folder.delete()
        # Redirect to the parent folder or the home page
        if parent_folder_id:
            return redirect('study_repository:home', folder_id=parent_folder_id)
        return redirect('study_repository:home')

    # Render confirmation page on GET request
    return render(request, 'study_repository/confirm_delete.html', {'folder': folder})

@login_required
def delete_file(request, file_id):
    # Get the file to delete
    file = get_object_or_404(File, id=file_id, owner=request.user)

    # Check if the file exists before trying to delete it
    if file.file:
        # Delete the file from the filesystem
        file.file.delete()

    # Delete the file record from the database
    file.delete()

    # Redirect back to the home page or the folder view
    return redirect('study_repository:home', folder_id=file.folder.id)
