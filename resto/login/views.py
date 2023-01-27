from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect

from login.forms import RegistrationForm


# UserCreationForm


# @login_required
def is_authenticated(request):
    if request.user.is_authenticated:
        return redirect('/settings')
    else:
        if User.objects.all().count() <= 1:
            return redirect('/registration')
        else:
            return redirect('/accounts/login/')


def registration(request):
    my_group = Group.objects.get(name='Admins')
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            if User.objects.all().count() <= 2:
                my_group.user_set.add(User.objects.last())
                return redirect('accounts/login/')
            else:
                return redirect('accounts/login/')
        else:
            error = 'Данные заполнены не верно'

    form = RegistrationForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/registration.html', data)
