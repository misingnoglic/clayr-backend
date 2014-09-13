import os

from django.shortcuts import render, HttpResponse
from django.conf import settings

from .forms import UploadFileForm
from ABBYY import process
from reader.testDB import testDatabaseGenerator
import json
import traceback


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
            loaded_json = parse_file(f,['wbc','rbc'])
            return HttpResponse(loaded_json, content_type='application/json')
    else:
        form = UploadFileForm()
    return render(request,'upload.html', {'form': form})

def parse_file(alias_found, tests):
    testDB = testDatabaseGenerator()
    results = {}
    words = alias_found.read().lower().split()
    for test in tests:
        value = None
        test_data = testDB[test.lower()]
        for alias in test_data.aliases:
            alias_found = False
            try:

                i = words.index(alias.lower())
                for x in range(i+1, i+5):#len(words)):
                    try:
                        value = float(words[x])
                        alias_found = True
                        break
                    except ValueError:
                        pass
                else:
                    pass


            except ValueError, err:
                pass

            if alias_found: break
        ranges = {}
        for t in test_data.ranges:
            ranges[t[0]]={'min':t[2][0], 'max':t[2][1], 'hex':t[1]}
        dictionary = {'value':value, 'brief_desc':test_data.brief_desc, 'ranges':ranges, 'unit':test_data.unit}
        results[test]=dictionary
    return json.dumps(results)


