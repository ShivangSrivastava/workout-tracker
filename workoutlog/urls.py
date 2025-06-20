"""
URL configuration for workoutlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import render
from django.urls import include, path


def custom_handler404(request, exception):
    return render(request, "404.html", status=404)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tracker.urls")),
    path("accounts/", include("accounts.urls")),
]

handler404 = custom_handler404
