from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def homepage(request):
    return HttpResponse("<h2>Домашняя страница</h2>")


def recipes(request, recipe):
    description = DATA.get(recipe)
    recipe_list = {}
    if description:
        servings = int(request.GET.get("servings", 1))
        for ingridient, amount in DATA[recipe].items():
            recipe_list[ingridient] = round(amount * servings, 2)
            print(ingridient, amount)
        context = {
            'recipe': recipe_list,
            'name': recipe
        }
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponseNotFound(f"Рецепт '{recipe}' не найден")
