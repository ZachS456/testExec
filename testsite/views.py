from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Exec(request):
  if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
          user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
          if user is not None:
              if user.is_active:
                  auth_login(request, user)
                  return render_to_response(
                  'home.html',
                  { 'user': request.user }
                  )
              else:
                  return render_to_response('register.html')
          else:
              return render_to_response('register.html')
      else:
          return render_to_response("login.html", {'form' : form})
  form = LoginForm()
  variables = RequestContext(request, {
    'form': form
  })
  return render_to_response("login.html", variables)
