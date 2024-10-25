from django.shortcuts import render, redirect

from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


def create_profile(request):
    form = ProfileCreateForm(request.POST or None)
    profile = Profile.objects.first()

    if profile:  # Plays the role of a guard so that noone can manually type the path in the url
        return redirect('home')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        "form": form,
        "profile": profile
    }

    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.first()

    if not profile:  # Plays the role of a guard so that noone can manually type the path in the url
        return redirect('home')

    context = {
        "profile": profile
    }
    return render(request, 'profiles/details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)

    if not profile:  # Plays the role of a guard so that noone can manually type the path in the url
        return redirect('home')

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {
        "form": form,
        "profile": profile
    }

    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()

    if not profile:  # Plays the role of a guard so that noone can manually type the path in the url
        return redirect('home')

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context ={
        "profile": profile
    }
    return render(request, 'profiles/delete-profile.html', context)