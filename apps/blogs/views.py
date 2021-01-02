from hitcount.views import HitCountDetailView

from django.views.generic import View
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from apps.blogs.models import Blog
# from apps.blogs.utils import verify_payment
from apps.payments.models import PaymentSuccessful


class BlogListView(ListView):
	model = Blog
	template_name = "blogs/homepage.html"

	def get_queryset(self):
		return Blog.objects.filter(level=0)


class BlogDetailSwitch(View):
	def get(self,request,slug):
		blog = get_object_or_404(Blog,slug=slug)
		if not blog.is_leaf_node():
			view = BlogDetailShowChildren.as_view()
			return view(request,slug=slug)
		else:
			view = BlogDetailView.as_view()
			return view(request,slug=slug)


class BlogDetailShowChildren(ListView):
	model = Blog
	template_name = "blogs/show_children.html"

	def dispatch(self,request,*args,**kwargs):
		self.blog = get_object_or_404(Blog,slug=self.kwargs.get("slug"))
		return super(BlogDetailShowChildren,self).dispatch(request,*args,**kwargs)

	def get_queryset(self):
		return self.blog.get_descendants(include_self=True).filter(is_active=True)

	def get_context_data(self,**kwargs):
		context_data = super(BlogDetailShowChildren,self).get_context_data(**kwargs)
		context_data["object"] = self.blog
		context_data["is_premium"] = self.check_premium_content()
		# context_data["has_access"] = self.check_access()
		context_data["ancestors"] = self.blog.get_ancestors()
		return context_data

	def check_premium_content(self):
		if not self.blog.is_free and self.blog.price:
			return True
		return False

	# def check_access(self):
	# 	payment_status = PaymentSuccessful.objects.filter(
	# 		blog__in= self.blog.get_ancestors(include_self=True),
	# 		user= self.request.user).exists()
	# 	return payment_status



# @method_decorator(login_required,name='dispatch')
# @method_decorator(verify_payment, name='dispatch')
class BlogDetailView(HitCountDetailView):
	queryset = Blog.objects.filter(is_active=True)
	template_name = "blogs/detail.html"
	count_hit = True

	def get_context_data(self,**kwargs):
		context = super(BlogDetailView,self).get_context_data(**kwargs)
		context["ancestors"] = self.object.get_ancestors()
		return context


def payment_required(request,slug):
	blog = get_object_or_404(Blog,slug=slug)
	context = {"blog":blog}
	return render(request,"blogs/payment_required.html",context)
