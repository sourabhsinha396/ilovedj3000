from django.urls import path

from apps.general_pages import views

app_name = 'general_pages'

urlpatterns = [
	path('contact/',views.ContactMeCreateView.as_view(),name="contact"),
]
