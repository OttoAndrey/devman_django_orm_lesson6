from django.contrib import admin
from django.utils.html import format_html

from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes']
    readonly_fields = ['get_image_preview']

    def get_image_preview(self, obj):
        if not obj.image or not obj.id:
            return 'нет картинки'
        return format_html('<img src="{src}" height="200"/>', src=obj.image.url)
    get_image_preview.short_description = 'превью'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post', 'author']


admin.site.register(Tag)
