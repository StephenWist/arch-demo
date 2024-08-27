from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from models.models import DatasetSeries

def image_upload(request):
    if request.method == "GET":
        dataset = DatasetSeries.objects.all()

        return render(request, 'upload.html', context={'datasets': dataset})