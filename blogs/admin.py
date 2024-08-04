from django.contrib import admin
from blogs.models import Category, Blog


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'updated_at')


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status','is_featured')
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
