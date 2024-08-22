from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from models import *


# def sf_detail(request, pk):
#     file_name = SoftFile.objects.get(pk=pk)
#     context = { 'file': file_name }
#     return return(request, 'upload.html', context)

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    if request.method == "POST" and 'run_eutils' in request.POST:
        pass
        # import script
        # from .. import eutils.sh

        # do the thing
        # eutils_runner(input)

        # reload page
        # return HttpResponseRedirect(reverse(app_name:view_name))

    return render(request, "upload.html", {
        "img_url": "/home/app/web/mediafiles/arch.png"
    })
