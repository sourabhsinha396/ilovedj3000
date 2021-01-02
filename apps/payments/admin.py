from django.contrib import admin

from apps.payments.models import PaymentSuccessful,PaymentAttempt

admin.site.register(PaymentAttempt)
admin.site.register(PaymentSuccessful)