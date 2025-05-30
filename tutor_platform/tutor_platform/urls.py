from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),  # Главная страница
    path('repetitor/', views.repetitor, name='repetitor'),
    path('student/', views.student, name='student'),
    path('repetitor/forgot_password/', views.forgot_password, name='forgot_password'),  # Добавление забытых паролей для репетиторов
    path('student/forgot_password/', views.forgot_password, name='forgot_password_student'),  # Для студентов
    path('repetitor/register/', views.register, name='register'),  # Один путь для регистрации
    path('repetitor/register_student/', views.register, name='register_student'),  # Регистрация для студентов (если нужно)
    path('register/login', views.login_success, name='login'),  # Регистрация для студентов (если нужно)
    path('register/home', views.home, name='register_home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('myapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
