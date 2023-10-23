from django.shortcuts import render
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/registration_done.html', context={'new_user': new_user})
    user_form = UserRegistrationForm
    return render(request, 'accounts/register.html', context={'form': user_form})
