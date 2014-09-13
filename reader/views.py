from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
import Image
import pytesseract
import os
from time import sleep

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def handle_file(f):
    f = f.read()
    #i = Image.open(f)
    # pytesseract.image_to_string(i)

def results(request):
    return render(request,'results.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_file(request.FILES['file'])
            #i = Image.open('record.tif')
            #pytesseract.image_to_string(i)
            return HttpResponseRedirect('/results')
    else:
        form = UploadFileForm()
    return render(request,'upload.html', {'form': form})

# Create your views here.
