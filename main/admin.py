from django.contrib import admin

from .models import Post,  Review
from django.utils.safestring import mark_safe
from django import forms


class ReviewInline(admin.TabularInline):
    model=Review
    # extra=1
    # readonly_fields=("name", "email")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # list_display=('id', "name", 'email', "parent", 'post')
    list_display = ('name', 'email', 'text', 'post', 'photo', 'parent', 'modified_by_admin')
    list_filter = ('post',)
    readonly_fields=("name", "email")
    fieldsets = (
        (None, {'fields': ('name', 'email', 'text', 'photo', 'parent', 'post', 'modified_by_admin')}),
    )

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by_admin = True
        obj.save()


    
admin.site.register(Post)