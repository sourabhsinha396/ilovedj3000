from django.urls import path

from apps.payments.views import create_payment,success

app_name = "payments"
urlpatterns = [
    path('blog/<str:slug>/payment/',create_payment,name="payment"),
    path('success/<str:slug>/',success,name="success"),
]