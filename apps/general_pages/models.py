from django.db import models


class ContactMe(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField(max_length=150)
	subject = models.CharField(max_length=200)
	message = models.TextField()