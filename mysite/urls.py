from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^polls/', include("blog.urls" , namespace="polls")),#manageNitkroute
    url(r'^pastebin/', include("pastebin.urls" , namespace="pastebin")),#pastebin
    url(r'^tinymce/', include('tinymce.urls')),#pastebin
    url(r'^codefundo/', include("codefundo.urls" , namespace="codefundo")),#codefundo
    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
