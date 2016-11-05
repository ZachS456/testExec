from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.shortcuts import render_to_response


# Create your views here.
def Exec(request):
  if request.method == 'POST':
      word = subprocess.check_output(["python3", "miditest.py", '-fname', 'UserHash'])
  return render_to_response('button.html', {'word': word})
