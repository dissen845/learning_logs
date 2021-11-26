from django.contrib import admin
from .models import Topic, Titles, Discussion

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('text',)}

admin.site.register(Topic, PostAdmin)
admin.site.register(Titles)
admin.site.register(Discussion)