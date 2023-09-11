from django.db import models
from django.utils import timezone

class Dashboard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ToDo(models.Model):
    task = models.TextField()
    is_done = models.BooleanField(default=False)
    
    def mark_done(self):
        self.is_done = True
        self.save()

class Cart(models.Model):
    items = models.JSONField()
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)


