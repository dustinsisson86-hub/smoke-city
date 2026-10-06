from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    from django.db import models

class FeaturedProduct(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='featured/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
