"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# src/config/urls.py

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.apps import apps


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    
]
# print('Вывод путей OSCAR',apps.get_app_config('oscar').urls[0])
# --- ПОДКЛЮЧАЕМ OSCAR ---
# Используем i18n_patterns для поддержки языков.
# который возвращает правильный application.
urlpatterns += i18n_patterns(
    path('', include(apps.get_app_config('oscar').urls[0])),
    prefix_default_language=False,
)

# --- DEBUG НАСТРОЙКИ ---
if settings.DEBUG:
    # В режиме разработки Django может обслуживать статику и медиа-файлы
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
