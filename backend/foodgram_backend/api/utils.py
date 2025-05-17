import string


BASE62_ALPHABET = string.digits + string.ascii_letters
BASE = len(BASE62_ALPHABET)


def generate_shopping_list_content(ingredients_queryset):
    """
    Генерирует текстовое содержимое для файла списка покупок.
    Принимает queryset с агрегированными данными ингредиентов.
    Queryset должен содержать словари с ключами:
    'ingredient__name', 'ingredient__measurement_unit', 'total_amount'.
    """
    shopping_list_parts = ['Список покупок:\n']
    if not ingredients_queryset:
        shopping_list_parts.append('Ваш список пуст.')
        return "".join(shopping_list_parts)
    for item in ingredients_queryset:
        name = item.get('ingredient__name', 'Без названия')
        unit = item.get('ingredient__measurement_unit', 'шт.')
        total_amount = item.get('total_amount', 0)
        shopping_list_parts.append(
            f'\n- {name} ({unit}) — {total_amount}'
        )
    return "".join(shopping_list_parts)
