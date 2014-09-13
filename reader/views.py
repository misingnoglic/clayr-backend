from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def handle_file(f):
    pass

def results(request):
    return render(request,'results.html')

def upload_file(request):
    if request.method == 'POST':
        print 1
        form = UploadFileForm(request.POST, request.FILES)
        print 2
        if form.is_valid():
            print 3
            handle_file(request.FILES['file'])
            return HttpResponseRedirect('/results')
    else:
        form = UploadFileForm()
    return render(request,'upload.html', {'form': form})

# Create your views here.
