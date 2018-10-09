"""project URL Configuration

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
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home-page"),
    path('sales/', views.getTheSalesList, name="sales-list"),
    path('subCategory/<int:category_id>/', views.subCategory, name="subCategory-page"),
    path('rentingPage/', views.rentingPage, name="renting-page"),
    path('sales/details/<int:post_id>/', views.getPostSalesDetails, name='sales-detail'),
    path('rent/', views.getTheRentList, name="rent-list"),
    path('rent/details/<int:post_id>/', views.getPostRentDetails, name='rent-detail'),


]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

