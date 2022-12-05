from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('servicios/', include('servicios.urls')),
    path('tienda/', include('tienda.urls')),
    path('carro/', include('carro.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('pedidos/', include('carro.urls')),
    
]
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)