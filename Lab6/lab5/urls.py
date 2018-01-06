"""lab5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path
from django.conf.urls import url
from django.contrib import admin
from my_app.views import Horses, Main_page



urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^test/', Horses.as_view(), name='list_url'),
    re_path(r'^main/', Main_page.as_view(), name='main_url')
]

