from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.blogs import views

app_name = 'blogs'

urlpatterns = [
	path('',views.BlogListView.as_view(),name="home"),
	path('blog/<str:slug>/',views.BlogDetailSwitch.as_view(),name="detail"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)