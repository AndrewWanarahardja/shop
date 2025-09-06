from django.db import models

# Create your models here.
import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('products', 'Products'),
        ('new', 'New'),
        ('exclusive', 'Exclusive'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=100000)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='new')
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()