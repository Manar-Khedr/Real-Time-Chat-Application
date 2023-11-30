from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import SharedFile
from .forms import FileUploadForm
from room.models import Room

def file_list(request):
    files = SharedFile.objects.all()
    return render(request, 'file_sharing/file_list.html', {'files': files})

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'file_sharing/file_upload.html', {'form': form})

def file_download(request, file_id):
    shared_file = get_object_or_404(SharedFile, pk=file_id)
    response = HttpResponse(shared_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename={shared_file.file.name}'
    return response
