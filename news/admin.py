from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админка для новостного поста."""
    fieldsets = [
        (
            'Главное',
            {
                'fields': ['name', 'slug', 'description'],
            },
        ),
        (
            'Публикация',
            {
                'fields': ['pub_date', 'is_published'],
            },
        ),
        (
            'Основной контент',
            {
                'classes': ['collapse'],
                'fields': ['text'],
            },
        ),
        (
            'Даты',
            {
                'fields': ['create_date', 'update_date'],
            },
        ),
    ]
    list_display = ('pk', 'name', 'slug', 'is_published', "view_on_site")
    list_display_links = ('pk', 'name', 'slug')
    readonly_fields = ('create_date', 'update_date')
    date_hierarchy = 'pub_date'
    search_fields = ('name', 'slug', 'description')
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name',), }
    actions = ['set_public', 'unset_public']

    def view_on_site(self, obj):
        if obj.is_published and obj.pub_date <= timezone.now():
            return mark_safe(f'<a href="{obj.get_absolute_url()}" blank=true>Посмотреть</a>')

    view_on_site.short_description = 'Посмотреть на сайте'

    def set_public(self, request, queryset):
        queryset.update(is_published=True)

    set_public.short_description = 'Опубликовать посты'

    def unset_public(self, request, queryset):
        queryset.update(is_published=False)

    unset_public.short_description = 'Снять посты с публикации'
