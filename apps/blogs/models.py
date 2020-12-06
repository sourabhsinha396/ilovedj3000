from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.urls import reverse


class Blog(MPTTModel):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	image = models.ImageField(blank=True,null=True)
	description = models.CharField(max_length=200)
	content = RichTextUploadingField()
	is_active = models.BooleanField(default=False)
	is_free = models.BooleanField(default=False)
	price = models.PositiveSmallIntegerField(blank=True,null=True)

	class MPTTMeta:
		order_insertion_by = ['title']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("blogs:detail",kwargs={"slug":self.slug})