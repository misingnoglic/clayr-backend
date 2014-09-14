import os
import sys


from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpRequest
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .forms import UploadFileForm
from ABBYY import process
from reader.testDB import testDatabaseGenerator, testValueDictionary
import json
import calendar
import time
from base64 import decodestring

import base64
import cStringIO

from django.core.files.uploadedfile import InMemoryUploadedFile



PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

@csrf_exempt #To allow android uploading
def upload_file(request, product=None):
    """
    Main view, it takes an image upload and gives the JSON Data
    """
    if request.method == 'POST': #If the image was uploaded
        test_values = testValueDictionary()
        unique_id = str(calendar.timegm(time.gmtime())-10**6) #Creates unique ID
        form = UploadFileForm(request.POST, request.FILES) #Gets files from the form
        if form.is_valid() and form.is_multipart():
            save_file(request.FILES['file'],unique_id,product) #Saves the image to allow for image processing
            output_file = open(os.path.join(settings.MEDIA_ROOT,'uploaded',unique_id,'output.txt')) #opens the OCR
            loaded_json = parse_file(output_file,test_values['cbc'],unique_id)
            return HttpResponse(loaded_json, content_type='application/json')
        else:
            save_file(request.FILES['userfile'],unique_id,product) #Saves the image to allow for image processing
            output_file = open(os.path.join(settings.MEDIA_ROOT,'uploaded',unique_id,'output.txt')) #opens the OCR
            loaded_json = parse_file(output_file,test_values['cbc'],unique_id)
            return HttpResponse(loaded_json, content_type='application/json')
    else:
        form = UploadFileForm()
        return render(request,'upload.html', {'form': form})

def decode_file(request):
    if request.POST.get('file') and request.POST.get('name'):
        file = cStringIO.StringIO(base64.b64decode(request.POST['file']))
        image = InMemoryUploadedFile(file,
           field_name='file',
           name=request.POST['name'],
           content_type="image/jpeg",
           size=sys.getsizeof(file),
           charset=None)
        request.FILES[u'file'] = image
        return HttpResponseRedirect('reader.views.upload_file')
    else:
        return HttpResponse("Fuck Off")

def save_file(file, unique_id, product,path=os.path.join('uploaded')):
    new_path = os.path.join(settings.MEDIA_ROOT,path)
    print('Media root: ' + settings.MEDIA_ROOT)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    new_path = os.path.join(new_path,unique_id)
    os.mkdir(new_path)
    filename = 'image'
    if not (product is None): filename = filename+"64"
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

    ## tests ##
    try:
        if results['mcv']['value']>results['mcv']['ranges']['AVG']['max']:
            results['mcv']['desc']+= " - High MCV correlates with Vitamin B12 Deficiency"

        if results['mcv']['value']<results['mcv']['ranges']['AVG']['min'] and not results['mcv']['value'] is None:
            if results['rdw']['value']>results['rdw']['ranges']['AVG']['max']:
                results['mcv']['desc'] += " - Low MCV and high RDW correlates with Iron Deficiency"

        if results['hemo']['value']<results['hemo']['ranges']['AVG']['min']-4:
            if results['mcv']['value']>(results['mcv']['ranges']['AVG']['max']+results['mcv']['ranges']['AVG']['min'])/2.0:
                results['hemo']['desc'] += " - Very low Hemoglobin and higher MCV correlates with pernicious anemia"
            else:
                results['hemo']['desc'] += " - Very low Hemoglobin and lower MCV correlates with microcitic anemia"
    except KeyError:
        pass

    json_file = json.dumps(results)
    with open(os.path.join(settings.MEDIA_ROOT,'uploaded',unique_id,'json.txt'), 'w') as json_storage:
        json_storage.write(json_file)
    return json_file


