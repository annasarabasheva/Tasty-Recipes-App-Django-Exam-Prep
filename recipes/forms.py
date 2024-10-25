from django import forms

from recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author', )


class RecipeCreateForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ingredients'].help_text = "Ingredients must be separated by a comma and space."
        self.fields['ingredients'].widget.attrs['placeholder'] = "ingredient1, ingredient2, ..."

        self.fields['instructions'].widget.attrs['placeholder'] = "Enter detailed instructions here..."

        self.fields['cooking_time'].help_text = "Provide the cooking time in minutes."

        self.fields['image_url'].widget.attrs['placeholder'] = "Optional image URL here..."


class RecipeEditForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True