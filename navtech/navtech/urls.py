"""navtech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from myapp.views import RegisterApiView,LoginApiView,Upload_Data,Order_Info,GetLast3MonthInfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterApiView.as_view(),name='register'),
    path('login/',LoginApiView.as_view(),name='login'),
    path('upload_data/',Upload_Data.as_view(),name='upload_data'),
    path("get_info/", GetLast3MonthInfo.as_view(), name="get_info"),
]
