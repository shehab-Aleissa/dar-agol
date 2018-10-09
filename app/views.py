from django.shortcuts import render, redirect
from .models import Post, Category, SubCategory
from django.db.models import Q
# Create your views here.
def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'home.html', context)

def subCategory(request, category_id):
    category_obj = Category.objects.get(id=category_id)
    # theSubCategory = category_obj.subcategory_set.all()
    theSubCategory = SubCategory.objects.filter(category=category_obj)
    context = {
        'sub': theSubCategory
    }
    return render(request, 'subCategory.html', context)

def rentingPage(request):
    return render(request, 'rentingPage.html', context)

def getTheSalesList(request):
    list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        list = list.filter(
            Q(عنوان_الاعلان__icontains=query)|
            Q(المنطقة__icontains=query)
            
        ).distinct()
    context = {
        'list': list
    }
    return render(request, 'sales.html', context)

def getPostSalesDetails(request, post_id):
    item = Post.objects.get(id=post_id)
    context = {
        'item': item
    }
    return render(request, 'salesDetail.html', context)

def getTheRentList(request):
    list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        list = list.filter(
            Q(عنوان_الاعلان__icontains=query)|
            Q(المنطقة__icontains=query)
            
        ).distinct()
    context = {
        'list': list
    }
    return render(request, 'rent.html', context)
def getPostRentDetails(request, post_id):
    item = Post.objects.get(id=post_id)
    context = {
        'item': item
    }
    return render(request, 'rentDetail.html', context)
