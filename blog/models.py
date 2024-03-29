from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')
admin.site.register(BlogPost,BlogPostAdmin)
