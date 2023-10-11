from django.contrib import admin

from .models import Post,  Review
from django.utils.safestring import mark_safe
from django import forms


class ReviewInline(admin.TabularInline):
    model=Review
    extra=1
    readonly_fields=("name", "email")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('id', "name", 'email', "parent", 'post')
    readonly_fields=("name", "email")
admin.site.register(Post)