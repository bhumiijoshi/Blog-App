import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("users/", include("users.urls")),
]
if settings.DEBUG_TOOLBAR:

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
