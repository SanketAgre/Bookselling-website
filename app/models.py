from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.

def get_file_path(request,filename):
    original_filename=filename
    nowtime=datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    filename="%s%s"%(nowtime, original_filename)
    return os.path.join('uploads/',filename)
    
class Category(models.Model):
    slug=models.CharField(max_length=150, null=False, blank=False)
    cat_name=models.CharField(max_length=50, null=False, blank=False)
    image=models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description=models.TextField(max_length=500, null=False, blank=False)
    ststus=models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default, 1=Trending")
    meta_titile=models.TextField(max_length=500, null=False, blank=False)
    meta_desc=models.TextField(max_length=500, null=False, blank=False)
    meta_keywords=models.TextField(max_length=500, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.CharField(max_length=150, null=False, blank=False)
    prod_name=models.CharField(max_length=150, null=False, blank=False)
    image=models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description=models.TextField(max_length=500, null=False, blank=False)
    small_desc=models.TextField(max_length=500, null=False, blank=False)
    quantity=models.IntegerField(null=False, blank=False)
    original_price=models.FloatField(null=False, blank=False)
    selling_price=models.FloatField(null=False, blank=False)
    ststus=models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default, 1=Trending")
    tag=models.CharField(max_length=150, null=False, blank=False)
    meta_titile=models.CharField(max_length=150, null=False, blank=False)
    meta_desc=models.CharField(max_length=150, null=False, blank=False)
    meta_keywords=models.CharField(max_length=150, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.prod_name


