# Python imports
# Django imports
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core import urls as core_urls
# Libraries imports
# App imports
from courses import urls as courses_urls
from topics import urls as topics_urls


admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', include((core_urls, 'core'), namespace='core')),
    path('turmas/', include((courses_urls, 'courses'), namespace='courses')),
    path('disciplinas/', include((topics_urls, 'topics'), namespace='topics')),
    path('accounts/', include('allauth.urls')),
    # path("", hello.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns