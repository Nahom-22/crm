
from django.contrib import admin
from django.urls import path, include
import crmapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(crmapp.urls.extraurlpatterns)),
    path('dashboard/', include(crmapp.urls.extraurlpatterns)),
    path('customers/', include(crmapp.urls.extraurlpatterns)),
    path('login/', include(crmapp.urls.extraurlpatterns)),
    path('register/', include(crmapp.urls.extraurlpatterns)),
    
        
]
