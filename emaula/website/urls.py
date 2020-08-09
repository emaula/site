"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.contrib.auth import views


urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/school/', permanent=True)),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/login/$', views.LoginView, name='login'),
    re_path(r'^school/', include('school.urls')),
    re_path(r'^lessons/', include('lessons.urls')),
    # Redireciona a home para a nossa aplicação:
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# STATIC URL STATIC ROOT para servir arquivos estáticos in development

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
