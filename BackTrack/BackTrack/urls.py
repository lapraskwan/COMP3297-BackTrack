"""BackTrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from PBI.views import main_view, add_view, detail_view, delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('PBI/',main_view),
    path('AddPBI/',add_view),
    path('BackToMainPBI',main_view),
    path('PBI/detail/<int:id>',detail_view),
    path('PBI/delete/<int:id>',delete_view),
    # path('PBI/', include('PBI.urls')),
    path('sprint_backlog/', include('sprint_backlog.urls')),
]
