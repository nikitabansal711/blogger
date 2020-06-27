"""SecondDjangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from blog import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),

]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
