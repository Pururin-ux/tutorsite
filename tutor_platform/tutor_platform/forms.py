from django import forms

class StudentLoginForm(forms.Form):
    email = forms.EmailField(label="Электронная почта", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class TutorLoginForm(forms.Form):
    email = forms.EmailField(label="Электронная почта", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
