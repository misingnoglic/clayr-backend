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

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def handle_file(f):
    i = ImageFile(f)
    print i.name
    print os.getcwd()
    image = Image.open(i)
    print image
    s = pytesseract.image_to_string(image)
    print s

def results(request):
    return render(request,'results.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            s = handle_file(request.FILES['file']) #Assume this function takes the image and gets text from it

            #Create a list of Tests and generate them
            #Call a function to find the values of those tests, if found add the file to the list


            return HttpResponseRedirect('/results')
    else:
        form = UploadFileForm()
    return render(request,'upload.html', {'form': form})

# Create your views here.
