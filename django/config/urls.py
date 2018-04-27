from django.conf import settings
from django.conf.urls.static import (
    static, )
from django.contrib import admin
from django.contrib.staticfiles.urls import (
    staticfiles_urlpatterns,
)
from django.urls import (
    include,
    path,
)

import core.urls
import user.urls

MEDIA_FILE_PATHS = static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(
        user.urls, namespace='user')),
    path('', include(
        core.urls, namespace='core')),
]
urlpatterns += MEDIA_FILE_PATHS
urlpatterns += staticfiles_urlpatterns()

try:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/',
             include(debug_toolbar.urls)),
    ]
except ImportError:
    pass


