from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.shortcuts import render_to_response
from .forms import AlgorithmForm
import os
from .choices import *
from django.contrib.sessions.backends.db import SessionStore

s = SessionStore()
# Create your views here.
def foo():
    try:
        foo.counter += 1
        return foo.counter
    except AttributeError:
        foo.counter = 1
        return foo.counter
def Exec(request):
    if request.method == 'POST':
        form = AlgorithmForm(request.POST)
        s.create()
        if form.is_valid():
            filename = s.session_key
            length = form.cleaned_data['length']
            if length is None:
                length = 6
            pathToMid = subprocess.check_output(["python3", "miditest.py", '-fname', filename, '-l', str(length)])
            pathToMid = pathToMid.decode("utf-8")
            pathToMid = pathToMid.strip()
            #font = FONT_CHOICES[int(form.cleaned_data['font'])-1][1]
            #pathToFont = os.path.dirname(os.path.abspath(__file__))
            #pathToFont += '/fonts/'
            #pathToFont += font
            #pathToFont += '.sf2'
            #filetype = OUTPUT_CHOICES[int(form.cleaned_data['output'])-1][1]
            #filename += filetype
            #if filetype != '.mid':
        #        words = subprocess.check_output(['fluidsynth','-T', filetype[1:], '-F', filename, '-ni', pathToFont, str(pathToMid)])
            return HttpResponse(pathToMid)
    else:
        form = AlgorithmForm();

    return render(request, 'button.html', {'form' : form})

def Result(request):
    return render(request, 'player.html', {})
