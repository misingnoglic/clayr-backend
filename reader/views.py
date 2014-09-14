import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

from django.shortcuts import render, HttpResponse
from django.conf import settings

from .forms import UploadFileForm
from ABBYY import process
from reader.testDB import testDatabaseGenerator
import json
import calendar
import time



# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file
def save_file(file, unique_id, path=os.path.join('uploaded')):
    new_path = os.path.join(settings.MEDIA_ROOT,path)
    print('Media root: ' + settings.MEDIA_ROOT)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    new_path = os.path.join(new_path,unique_id)
    os.mkdir(new_path)
    filename = 'image'
    filepath = os.path.join(str(new_path), str(filename))
    fd = open(filepath, 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
    handle_file(filepath)

def handle_file(filename):
    path = os.path.split(filename)[0]
    process.recognizeFile(filename,path)

def results(request):
    return render(request,'results.html')

def upload_file(request):
    if request.method == 'POST':
        unique_id = str(calendar.timegm(time.gmtime())-10**6)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():

            save_file(request.FILES['file'],unique_id)

            f = open(os.path.join(settings.MEDIA_ROOT,'uploaded',unique_id,'output.txt'))
            loaded_json = parse_file(f,['wbc','rbc'],unique_id)
            return HttpResponse(loaded_json, content_type='application/json')
    else:
        form = UploadFileForm()
    return render(request,'upload.html', {'form': form})

def parse_file(alias_found, tests,unique_id):
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
                for x in range(i+1, i+5):
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
        dictionary = {'value':value, 'brief_desc':test_data.brief_desc, 'desc':test_data.desc,
                      'ranges':ranges, 'unit':test_data.unit}
        results[test]=dictionary
    results['id']= unique_id
    json_file = json.dumps(results)
    with open(os.path.join(settings.MEDIA_ROOT,'uploaded',unique_id,'json.txt'), 'w') as json_storage:
        json_storage.write(json_file)
    return json_file
