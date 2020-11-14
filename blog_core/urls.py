from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('adminra/', admin.site.urls),
    path('',include("apps.blogs.urls")),
    path('',include("apps.general_pages.urls")),
]
