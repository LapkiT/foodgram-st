from django.shortcuts import get_object_or_404, redirect
from django.views import View

from .models import Recipe


class RecipeShortLinkView(View):
    """
    Представление для обработки коротких ссылок на рецепты.
    Перенаправляет на страницу рецепта по его ID.
    """

    def get(self, request, short_id):
        """
        Обрабатывает GET-запрос к короткой ссылке.
        Декодирует short_id в ID рецепта и перенаправляет на страницу рецепта.
        """
        try:
            recipe_id = int(short_id)
        except ValueError:
            return redirect('home')

        recipe = get_object_or_404(Recipe, id=recipe_id)
        return redirect('recipe-detail', pk=recipe.id)
