"""Api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fun),
    path('fun',views.fun1),
    path('fun1',views.fun2),
    path('fun3/<d>',views.fun3),
    path('fun4',views.fun4),
    path('fun5/<d>',views.fun5),
    path('fun6',views.fun6.as_view()),
    path('fun7/<d>',views.fun7.as_view()),
    path('fun8',views.genericapiview.as_view()),
    path('fun9/<id>',views.update.as_view()),

]
