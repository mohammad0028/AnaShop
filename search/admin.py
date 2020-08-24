from django.contrib import admin
from search.models import Tag


# Register your models here.


class TagAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'products']
    list_display = ['id', '__str__', 'slug', 'get_list_of_products']

    def get_list_of_products(self, obj):
        return " - \n".join([p.title for p in obj.products.all()])

    class Meta:
        model = Tag


admin.site.register(Tag, TagAdmin)
