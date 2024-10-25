from django.shortcuts import render, redirect

from profiles.models import Profile
from recipes.forms import RecipeCreateForm
from recipes.models import Recipe


def catalogue(request):
    all_recipes = Recipe.objects.all()
    context = {
        "all_recipes": all_recipes
    }
    return render(request, 'recipes/catalogue.html', context)


def create_recipe(request):
    form = RecipeCreateForm(request.POST or None)
    profile = Profile.objects.first()

    if request.method == 'POST':
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = profile
            recipe.save()
            return redirect('catalogue')

    context = {
        "form": form
    }

    return render(request, 'recipes/create-recipe.html', context)


def details_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    context = {
        "recipe": recipe
    }
    return render(request, 'recipes/details-recipe.html', context)


def edit_recipe(request, recipe_id):
    pass


def delete_recipe(request, recipe_id):
    pass