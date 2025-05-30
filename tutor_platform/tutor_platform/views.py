from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def repetitor(request):
    return render(request, 'repetitor.html')

def student(request):
    return render(request, 'student.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')
def register(request):
    return render(request, 'register.html')

def login_success(request):
    return render(request, 'login.html')

def logout_success(request):
    return render(request, 'logout.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import StudentLoginForm, TutorLoginForm

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Перенаправление на главную страницу
            else:
                form.add_error(None, "Неверный логин или пароль")
    else:
        form = StudentLoginForm()
    return render(request, 'student_login.html', {'form': form})

def tutor_login(request):
    if request.method == 'POST':
        form = TutorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Неверный логин или пароль")
    else:
        form = TutorLoginForm()
    return render(request, 'tutor_login.html', {'form': form})

