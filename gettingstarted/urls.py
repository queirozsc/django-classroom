from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from core import urls as core_urls
admin.autodiscover()

#import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', include((core_urls, 'core'), namespace='core')),
    # path("", hello.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns