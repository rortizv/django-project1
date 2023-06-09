"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Project1.views import say_hello, say_goodbye, get_date, calc_age, javascript_course, angular_course


urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting/', say_hello),
    path('goodbye/', say_goodbye),
    path('date/', get_date),
    path('calc_age/<int:age>/<int:year>', calc_age),
    path('javascript_course/', javascript_course),
    path('angular_course/', angular_course),
]
