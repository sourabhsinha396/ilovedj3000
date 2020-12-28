import uuid
import os
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadWrapper(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[-1]
        return self.path % (uuid.uuid4(), extension)
