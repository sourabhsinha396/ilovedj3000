from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.blogs.models import Blog


class BlogSitemap(Sitemap):
    changefreq = "yearly"

    def items(self):
        return Blog.objects.filter(is_active=True)

    def lastmod(self,item):
        return item.updated 

    def location(self,item):
        return item.get_absolute_url()

    def priority(self,item):
        if item.is_root_node():
            return 0.9
        return 0.8


class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = "yearly"

    def items(self):
        return ("general_pages:contact",)

    def location(self,item):
        return reverse(item)