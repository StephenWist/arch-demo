from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from models.models import DatasetSeries

# def sf_detail(request, pk):
#     file_name = SoftFile.objects.get(pk=pk)
#     context = { 'file': file_name }
#     return return(request, 'upload.html', context)

def image_upload(request):
    if request.method == "GET":
        dataset = DatasetSeries.objects.all()

        return render(request, 'upload.html', context={'datasets': dataset})
    # if request.method == "POST" and 'run_eutils' in request.POST:
    #     pass
        # import script
        # from .. import eutils.sh

        # do the thing
        # eutils_runner(input)

        # reload page
        # return HttpResponseRedirect(reverse(app_name:view_name))
