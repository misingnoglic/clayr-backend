from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files import File
from django.core.files.images import ImageFile
from django.shortcuts import render_to_response
from .forms import UploadFileForm
import Image
import pytesseract
import os
from logic import Test
from time import sleep
from ABBYY import process
from django.conf import settings

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file
def save_file(file, path='uploaded/'):
    os.mkdir(settings.MEDIA_ROOT+"/"+path)
    filename = file._get_name()
    fd = open('%s/%s' % (settings.MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
    handle_file('%s/%s' % (settings.MEDIA_ROOT, str(path) + str(filename)))

def handle_file(filename):
    path = os.path.split(filename)[0]
    process.recognizeFile(filename,path)


def results(request):
    return render(request,'results.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():
            save_file(request.FILES['file']) #Assume this function takes the image and gets text from it
            #return HttpResponse("THanks!")
            #Create a list of Tests and generate them
            #Call a function to find the values of those tests, if found add the file to the list
            return HttpResponseRedirect('/results')
            #return HttpResponse(content, content_type='text/plain')
    else:
        form = UploadFileForm()
    return render(request,'upload.html', {'form': form})

# Create your views here.
