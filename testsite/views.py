from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.shortcuts import render_to_response


# Create your views here.
def Exec(request):
  if request.method == 'POST':
      words = subprocess.check_output(["python3", "miditest.py", '-fname', 'UserHash'])
      return HttpResponse(words)
  else:
      return render(request, 'button.html')
