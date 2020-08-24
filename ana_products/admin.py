from django.contrib import admin
from .models import Category, SubCategory, Product, Images, Comment, Answer


# Register your models here.

class ProductImagesInline(admin.StackedInline):
    model = Images


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category', 'subcategory']
    list_filter = ['added_date', 'category']
    list_editable = ['price']
    inlines = [ProductImagesInline]


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'price', 'image']
#
#
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Images)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category']
    list_editable = ['category']


admin.site.register(Category)
admin.site.register(SubCategory, SubcategoryAdmin)


# -----------------------------------------------------------------------------------------------

# Comment and Answers
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer_name', 'product', 'id', 'body', 'timestamp', 'active')
    list_filter = ('active', 'timestamp')
    search_fields = ('writer_name', 'body')
    list_editable = ['active']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['reply_to', 'writer_name', 'id', 'timestamp', 'body']
    list_filter = ['writer_name']


admin.site.register(Answer, AnswerAdmin)
