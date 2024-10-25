from django.shortcuts import render, redirect

from profiles.models import Profile
from recipes.forms import RecipeCreateForm


def catalogue(request):
    return render(request, 'recipes/catalogue.html')


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



