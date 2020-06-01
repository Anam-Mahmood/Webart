from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views

urlpatterns = [
                path('', include('app.urls')),
                path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
