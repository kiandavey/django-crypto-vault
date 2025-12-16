from django.contrib import admin
from django.urls import path, include # <--- Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crypto.urls')), # <--- Send everything else to the crypto app
]