from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    عنوان_الاعلان = models.CharField(max_length=250)
    المنطقة = models.CharField(max_length=250)
    عدد_الغرف = models.IntegerField(blank=True, null=True)
    المساحه = models.IntegerField(blank=True, null=True)
    الموقع = models.CharField(max_length=250)
    الوصف = models.TextField()
    img = models.ImageField(null=True, blank=True)
    حالة_العقار = models.CharField(max_length=250)
    تاريخ_الاعلان = models.DateTimeField(auto_now=True)
    تاريخ_تعديل_الاعلان = models.DateTimeField(auto_now_add=True)
    خصوصي =  models.TextField(null=True, blank=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.عنوان_الاعلان
