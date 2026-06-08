from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lambda request: HttpResponse("Welcome to Internship Portal")),

    path('users/', include('users.urls')),
    path('internships/', include('internships.urls')),
    path('applications/', include('applications.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)