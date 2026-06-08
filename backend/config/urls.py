from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cursos.urls')),
    path('api/instrutores/', include('instrutor.urls')),
]
