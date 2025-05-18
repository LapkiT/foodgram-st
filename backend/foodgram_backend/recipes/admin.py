from django.contrib import admin
from django.utils.html import format_html, mark_safe

from .models import (
    Ingredient, Recipe, RecipeIngredient, Favorite, ShoppingCart
)


class BaseAdminSettings(admin.ModelAdmin):
    """Общие настройки для админ-панели"""

    empty_value_display = '-пусто-'
    list_per_page = 20


@admin.register(Ingredient)
class IngredientAdmin(BaseAdminSettings):
    """Админ-панель для модели Ingredient"""

    list_display = ('name', 'measurement_unit', 'recipes_count')
    search_fields = ('name', 'measurement_unit')
    list_filter = ('measurement_unit',)

    @admin.display(description='Число рецептов')
    def recipes_count(self, obj):
        return obj.recipes.count()


class RecipeIngredientInline(admin.TabularInline):
    """
    Инлайн для редактирования ингредиентов внутри рецепта.
    Позволяет добавлять/изменять/удалять ингредиенты и их количество.
    """

    model = RecipeIngredient

    fields = ('ingredient', 'amount')
    autocomplete_fields = ('ingredient',)
    extra = 1
    min_num = 1

    verbose_name = 'Ингредиент'
    verbose_name_plural = 'Ингредиенты рецепта'


@admin.register(Recipe)
class RecipeAdmin(BaseAdminSettings):
    """Админ-панель для модели Recipe"""

    list_display = (
        'id', 'name', 'cooking_time', 'author', 'favorited_count', 'get_products', 'get_image_preview'
    )

    readonly_fields = ('get_image_preview', 'favorited_count')
    search_fields = ('name', 'author__username')
    list_filter = ('author', 'name')
    inlines = [RecipeIngredientInline]

    ordering = ('-pub_date',)

    @admin.display(description='Первью изображения')
    def get_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="50" />', obj.image.url
            )
        return "Нет изображения"

    @admin.display(description='В избранном (раз)', ordering='favorited_by__count')
    def favorited_count(self, obj):
        return obj.favorited_by.count()

    @admin.display(description='Продукты')
    def get_products(self, obj):
        items = obj.recipe_ingredients.select_related('ingredient').all()
        html = '<ul>' + ''.join(
            f'<li>{ri.ingredient.name} — {ri.amount} {ri.ingredient.measurement_unit}</li>' for ri in items
        ) + '</ul>'
        return mark_safe(html)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Админ-панель для модели Favorite"""

    list_display = ('id', 'user', 'recipe')
    search_fields = ('user__username', 'recipe__name')
    list_filter = ('user', 'recipe')
    ordering = ('id',)
    autocomplete_fields = ('user', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Админ-панель для модели ShoppingCart"""

    list_display = ('id', 'user', 'recipe')
    search_fields = ('user__username', 'recipe__name')
    list_filter = ('user', 'recipe')
    ordering = ('id',)
    autocomplete_fields = ('user', 'recipe')
