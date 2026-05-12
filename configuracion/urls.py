from django.contrib import admin
from django.urls import path, include # Importante agregar 'include'
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jardin.urls')), # Esta línea conecta tu página principal con la app jardín
]

# Esto es lo que permite que las fotos se vean en el navegador
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    