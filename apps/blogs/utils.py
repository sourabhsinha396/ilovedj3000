import uuid
import os
from functools import wraps

from django.utils.deconstruct import deconstructible
from django.shortcuts import get_object_or_404
from django.apps import apps


@deconstructible
class UploadWrapper(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[-1]
        return self.path % (uuid.uuid4(), extension)


# def verify_payment(function):
#     def wrap(request, *args, **kwargs):
#         Blog = apps.get_model('blogs','Blog')
#         from apps.payments.models import PaymentSuccessful
#         from apps.blogs.views import payment_required
#         blog = get_object_or_404(Blog,slug=kwargs['slug'])
#         if not blog.is_free and blog.price:
#             payment = PaymentSuccessful.objects.filter(blog__in=blog.get_ancestors(include_self=True),user=request.user)
#             if payment.exists():
#                 return function(request, *args, **kwargs)
#             else:
#                 return payment_required(request,*args,**kwargs)
#     wrap.__doc__ = function.__doc__
#     return wrap


def disable_for_loaddata(signal_handler):
    @wraps(signal_handler)
    def wrapper(*args, **kwargs):
        print(args,kwargs)
        if kwargs.get('raw'):
            return
        signal_handler(*args, **kwargs)
    return wrapper