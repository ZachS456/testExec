from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.shortcuts import render_to_response
from .forms import AlgorithmForm
import uuid


# Create your views here.
def myfunc():
  myfunc.counter += 1
  return myfunc.counter
myfunc.counter = 0
def Exec(request):
    if request.method == 'POST':
        form = AlgorithmForm(request.POST)
        if form.is_valid():
            filename = form.cleaned_data['name'] 
            filename += ' - ' 
            filename += uuid.uuid4().hex[:6].upper()
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
