from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),  # добавьте маршрут для регистрации
    path('', include('core.urls')),  # другие маршруты вашего проекта
]
