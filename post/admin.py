from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'created_at', 'slug']
    list_display_links = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title','content']
    # list_editable =['title']
    class Meta:
        model =Post

admin.site.register(Post, PostAdmin)
