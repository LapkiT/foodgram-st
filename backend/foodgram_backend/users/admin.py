from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe


User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Кастомизация панели администратора для модели User.
    """

    list_display = (
        'id',
        'username',
        'full_name',
        'email',
        'avatar_tag',
        'recipes_count',
        'subscriptions_count',
        'followers_count',
        'is_staff',
        'is_active',
    )

    search_fields = ('username', 'email')

    list_filter = (
        'is_staff', 'is_superuser', 'is_active', 'groups',
    )

    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {
            'fields': ('first_name', 'last_name', 'email', 'avatar')
        }),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name',
                       'last_name', 'avatar', 'is_staff',
                       'is_superuser', 'groups',
                       'user_permissions'),
        }),
    )

    @admin.display(description='ФИО')
    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    @admin.display(description='Аватар')
    def avatar_tag(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="40" height="40" style="object-fit:cover; border-radius:50%;" />')
        return '-'

    @admin.display(description='Рецептов')
    def recipes_count(self, obj):
        return obj.recipes.count()

    @admin.display(description='Подписок')
    def subscriptions_count(self, obj):
        return obj.subscriptions.count()

    @admin.display(description='Подписчиков')
    def followers_count(self, obj):
        return obj.subscribers.count()
