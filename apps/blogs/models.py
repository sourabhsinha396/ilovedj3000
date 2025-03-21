import sys
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image
from io import BytesIO

from django.db import models
from django.urls import reverse
from django.forms import ValidationError
from django.dispatch import receiver
from django.db import transaction
from django.db.models.signals import pre_save
from django.core.files.uploadedfile import InMemoryUploadedFile

from apps.blogs.utils import UploadWrapper,disable_for_loaddata


class Blog(MPTTModel):
	type_choices = (
		(1,"Blog"),
		(2,"Projects"),
	)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	type_of = models.IntegerField(choices=type_choices,default=1)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	image = models.ImageField(upload_to = UploadWrapper('thumbnails'), blank=True,null=True)
	description = models.CharField(max_length=200)
	content = RichTextUploadingField()
	is_active = models.BooleanField(default=False)
	is_free = models.BooleanField(default=False)
	price = models.PositiveSmallIntegerField(blank=True,null=True,help_text="In INR")
	updated = models.DateTimeField(auto_now=True)

	class MPTTMeta:
		order_insertion_by = ['title']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("blogs:detail",kwargs={"slug":self.slug})

	def clean(self):
		if not self.is_free and not self.price:
			raise ValidationError("Provide either free or price.")

	def get_active_previous_sibling(self):
		previous = self.get_previous_sibling()
		if previous and previous.is_active:
			return previous

	def get_active_next_sibling(self):
		next = self.get_next_sibling()
		if next and next.is_active:
			return next


@receiver(pre_save, sender=Blog)
@disable_for_loaddata
@transaction.atomic
def compress_uploaded_image(sender, instance, **kwargs):
    try:
        article = sender.objects.select_for_update().get(pk=instance.pk)
    except sender.DoesNotExist:
        # Its a new object
        if instance.image:
        	instance.image = compress_image(instance.image)
    else:
        if instance.image and article.image != instance.image:
            instance.image = compress_image(instance.image)


def compress_image(uploaded_image):
    image = Image.open(uploaded_image)
    temp_image = image.convert('RGB')
    temp_image = temp_image.resize((1080,570))
    output_io_stream = BytesIO()
    temp_image.save(output_io_stream , format='JPEG', quality=60)
    output_io_stream.seek(0)
    compressed = InMemoryUploadedFile(output_io_stream,'ImageField', "%s.jpg" % uploaded_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output_io_stream), None)
    return compressed


@receiver(models.signals.post_delete, sender=Blog)
def remove_image_from_s3(sender, instance, using, **kwargs):
	instance.image.delete(save=False)
