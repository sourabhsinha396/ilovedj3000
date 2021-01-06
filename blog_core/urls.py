from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from apps.seo.sitemaps import BlogSitemap, StaticSitemap

sitemaps = {
    "blog_sitemap":BlogSitemap,
    "static_urls":StaticSitemap,
}

urlpatterns = [
    path('adminra/', admin.site.urls),
    path('',include("apps.blogs.urls")),
    path('',include("apps.general_pages.urls")),
    path('',include("apps.payments.urls")),
    path('',include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)