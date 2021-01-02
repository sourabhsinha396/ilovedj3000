from django.db import models
from django.conf import settings


class PaymentSuccessful(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
	blog = models.ForeignKey("blogs.Blog",on_delete=models.SET_NULL,null=True)
	amount = models.DecimalField(max_digits=6,decimal_places=2)
	currency = models.CharField(max_length=20)
	geteway_name = models.CharField(max_length=30,blank=True,null=True)
	payment_id = models.CharField(max_length=255)
	order_id = models.CharField(max_length=255)
	status = models.CharField(max_length=30)
	extra = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.user.username + str(self.amount)


class PaymentAttempt(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
	blog = models.ForeignKey("blogs.Blog",on_delete=models.CASCADE)
	order_id = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.user.username
