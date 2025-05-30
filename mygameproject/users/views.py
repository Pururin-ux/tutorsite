# views.py

from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на страницу home.html после успешной регистрации
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

