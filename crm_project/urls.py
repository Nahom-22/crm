
from django.contrib import admin
from django.urls import path
import crmapp
import crmapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', crmapp.urls.urlpatterns[1]),
    path('login/', crmapp.urls.urlpatterns[3]),
    path('register/',crmapp.urls.urlpatterns[4]),        
        
]
