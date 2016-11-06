from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.shortcuts import render_to_response
from .forms import AlgorithmForm
import uuid


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
        if form.is_valid():
            filename = form.cleaned_data['name'] 
            filename += ' - ' 
            filename += str(foo())
            length = form.cleaned_data['length']
            if length is None:
                length = 6
            start = form.cleaned_data['start']
            if start is '':
                start = 'RAND'
            words = subprocess.check_output(["python3", "miditest.py", '-fname', filename, '-l', str(length), '-s', start])
            return HttpResponse(words)
    else:
        form = AlgorithmForm();

    return render(request, 'button.html', {'form' : form})
