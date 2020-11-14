from hitcount.views import HitCountDetailView

from django.views.generic import View
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404


from apps.blogs.models import Blog


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

	def get_queryset(self):
		return Blog.objects.get(slug=self.kwargs.get('slug')).get_descendants(include_self=True)


class BlogDetailView(HitCountDetailView):
	queryset = Blog.objects.filter(is_active=True)
	template_name = "blogs/detail.html"
	count_hit = True