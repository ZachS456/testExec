from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^Exec/$', views.Exec, name="Exec"),
    url(r'^Result/$', views.Result, name="Result"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
