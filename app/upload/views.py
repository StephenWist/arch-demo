from django.shortcuts import render
from django.http import HttpResponseRedirect

from models.models import DatasetSeries

def image_upload(request):
    if request.method == "GET":
        dataset = DatasetSeries.objects.all()

        return render(request, 'upload.html', context={'datasets': dataset})
    if request.method == "POST":
        import subprocess
        subprocess.call(['sh', 'staticfiles/ftp_geo.sh'])
        return render(request, 'upload.html')