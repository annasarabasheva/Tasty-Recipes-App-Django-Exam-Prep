from django.shortcuts import render, redirect

from profiles.models import Profile
from recipes.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipes.models import Recipe


def catalogue(request):
    all_recipes = Recipe.objects.all()
    profile = Profile.objects.first()

    if not profile:  # Plays the role of a guard so that noone can manually type the path in the url
        return redirect('home')

    context = {
        "all_recipes": all_recipes,
        "profile": profile
    }
    return render(request, 'recipes/catalogue.html', context)


def create_recipe(request):
    form = RecipeCreateForm(request.POST or None)
    profile = Profile.objects.first()

    if not profile:  # Plays the role of a guard so that noone can manually type the path in the url
        return redirect('home')

    if request.method == 'POST':
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = profile
            recipe.save()
            return redirect('catalogue')

    context = {
        "form": form,
        "profile": profile
    }

    return render(request, 'recipes/create-recipe.html', context)


def details_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    profile = Profile.objects.first()


    if not profile:  # Plays the role of a guard so that noone can manually type the path in the url
        return redirect('home')

    context = {
        "recipe": recipe,
        "profile": profile

    }
    return render(request, 'recipes/details-recipe.html', context)


def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeEditForm(request.POST or None, instance=recipe)
    profile = Profile.objects.first()

    if not profile:  # Plays the role of a guard so that noone can manually type the path in the url
        return redirect('home')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        "form": form,
        "profile": profile
    }
    return render(request, 'recipes/edit-recipe.html', context)


def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeDeleteForm(request.POST or None, instance=recipe)
    profile = Profile.objects.first()

    if not profile:  # Plays the role of a guard so that noone can manually type the path in the url
        return redirect('home')

    if request.method == 'POST':
        recipe.delete()
        return redirect('catalogue')

    context = {
        "form": form,
        "profile": profile
    }

    return render(request, 'recipes/delete-recipe.html', context)