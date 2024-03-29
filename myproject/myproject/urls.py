from django.contrib import admin
from django.urls import include, path
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
    path('users/', include("users.urls")),
]
if settings.DEBUG_TOOLBAR:
    
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
