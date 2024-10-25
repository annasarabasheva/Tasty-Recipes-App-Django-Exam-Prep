from django.shortcuts import render, redirect

from profiles.forms import ProfileCreateForm


def create_profile(request):
    form = ProfileCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        "form": form
    }

    return render(request, 'profiles/create-profile.html', context)