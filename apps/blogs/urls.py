from django.urls import path

from apps.blogs import views

app_name = 'blogs'

urlpatterns = [
	path('',views.BlogListView.as_view(),name="home"),
	path('blog/<str:slug>/',views.BlogDetailSwitch.as_view(),name="detail"),
]