from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from apps.blogs.models import Blog

from django.contrib import admin


admin.site.register(
    Blog,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)



