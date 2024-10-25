from django import forms

from recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author', )


class RecipeCreateForm(RecipeBaseForm):
    pass

