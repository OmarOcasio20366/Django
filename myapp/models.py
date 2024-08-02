from django.db import models
from django.db.models import JSONField

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length = 13)
    
    def __str__(self):
        return self.title
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to = 'uploads/')
    uploaded_at = models.DateTimeField(auto_now_add = True)
    
class Product(models.Model):
    name = models.CharField(max_length = 255)
    specifications = JSONField()
    
    def __str__(self):
        return self.name
    
    
# class Event(models.Model):
#     name = models.CharField(max_length = 255)
#     participants = ArrayField(models.CharField(max_length = 255), blank = True)
    
#     def __str__(self):
#         return self.name
    
    
class MyModel(models.Model):
    name = models.CharField(max_length = 255)
    specifications = JSONField()
    
    def __str__(self):
        return self.name