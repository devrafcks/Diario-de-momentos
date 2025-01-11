from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('diario', permanent=True)),
    path('diario/', include('diario.urls')),
    path('admin/', admin.site.urls),
    path('diario/', include('diario.urls')),
    path('', lambda request: redirect('diario'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)