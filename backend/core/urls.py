from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('supersecret/', admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header= 'HEES Admin'
admin.site.site_title= 'HEES Admin Portal'
admin.site.index_title= 'Welcome to the HEES Admin Portal'