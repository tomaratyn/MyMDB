from django.urls import path, include
from django.contrib import admin

import core.urls
import user.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(
        user.urls, namespace='user')),
    path('', include(
        core.urls, namespace='core')),
]
