from django.shortcuts import redirect
from .models import Recipe

def recipe_short_link(request, short_id):
    """
    Обрабатывает GET-запрос к короткой ссылке.
    Перенаправляет на страницу рецепта по его ID, если такой рецепт есть.
    """
    try:
        recipe_id = int(short_id)
    except (ValueError, TypeError):
        return redirect('home')
    if Recipe.objects.filter(id=recipe_id).exists():
        return redirect(f'/recipes/{recipe_id}/')
    return redirect('home')
