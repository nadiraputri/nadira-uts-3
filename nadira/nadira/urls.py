from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.putri),
    path('makanan/', include('makanan.urls')),
    path('minuman/', include('minuman.urls')),
    path('kantin/', include('kantin.urls')),
]