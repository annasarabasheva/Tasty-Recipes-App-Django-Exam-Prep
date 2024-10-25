from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('bio', )


class ProfileCreateForm(ProfileBaseForm):
    pass