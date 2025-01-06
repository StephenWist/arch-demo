from django.shortcuts import render
from django.http import HttpResponseRedirect
import subprocess
from models.models import DatasetSeries

def image_upload(request):
    if request.method == "GET":
        dataset = DatasetSeries.objects.all()

        return render(request, 'upload.html', context={'datasets': dataset})
    if request.method == "POST":
        
        subprocess.call(['sh', 'staticfiles/ftp_geo.sh'])
        # call data processing code here
        
        dataset = DatasetSeries.objects.all()
        return render(request, 'upload.html', context={'datasets': dataset})