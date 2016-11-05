from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^Exec/', views.Exec, name="Exec"),
]
