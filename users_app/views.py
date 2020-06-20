from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        # process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            # log user in and redirect to home Page
            login(request, new_user)
            return redirect('dj_map_app:index')

    # Display blank form or invalid
    context = {'form': form}
    return render(request, 'registration/register.html', context)
