from django.conf.urls import url
from django.contrib import admin
from tutorial.views import people,games

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^people/', people),
    url(r'^games/', games)
]
