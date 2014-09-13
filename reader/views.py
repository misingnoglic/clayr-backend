from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
import os
from ABBYY import process
from django.conf import settings
from testDB import testDatabaseGenerator

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
            #return HttpResponseRedirect('/results')
            f = open("media/uploaded/output.txt")
            return HttpResponse(f, content_type='text/plain')
    else:
        form = UploadFileForm()
    return render(request,'upload.html', {'form': form})

def parse_file(f, tests):
    testDB = None #I'll deal with this later
    results = {}
    string = f.read().split()
    for test in tests:
        test_data = testDB['test']
        for alias in test_data.aliases:
            try:
                i = string.index(alias)
                for x in range(i,string.length()):
                    try:
                        value = int(string[x])
                        break
                    except ValueError:
                        pass

# Create your views here.
