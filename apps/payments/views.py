import os
import razorpay

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from apps.blogs.models import Blog
from apps.payments.forms import PaymentDetailForm
from apps.payments.models import PaymentAttempt,PaymentSuccessful
from apps.payments.utils import get_currency_amount


@login_required
def create_payment(request,slug):
	blog = get_object_or_404(Blog,slug=slug)
	if request.method == "POST":
		form = PaymentDetailForm(request.POST)
		if form.is_valid():
			client = razorpay.Client(auth=(os.getenv('rzrpaykey'), os.getenv('rzrsecret')))
			currency = form.cleaned_data.get("currency")
			amount = get_currency_amount(currency,blog.price)
			response = client.order.create({'amount':amount,'currency':currency,'payment_capture':1})
			print(response)
			PaymentAttempt.objects.create(user=request.user,blog=blog,order_id=response["id"])
			context = {'form':form,'response':response,'blog':blog}
			return render(request,"payments/payment_init.html",context)
		else:
			print(form.errors)
			return render(request,"payments/payment_init.html")

	form = PaymentDetailForm()
	context = {'form':form}
	return render(request,"payments/payment_init.html",context)



@csrf_exempt
def success(request,slug):
	blog = get_object_or_404(Blog,slug=slug)
	if request.method =="POST":
		client = razorpay.Client(auth=(os.getenv('rzrpaykey'), os.getenv('rzrsecret')))
		payment = client.payment.fetch(request.POST.get("razorpay_payment_id"))
		PaymentSuccessful.objects.create(
			user = request.user,
			blog = blog,
			amount = payment.get("amount"),
			currency = payment.get("currency"),
			geteway_name = "Razorpay",
			payment_id = payment.get("id"),
			order_id=payment.get("order_id"),
			status = payment.get("status"),
			extra=str(payment)
		)
		return render(request,"payments/success.html")