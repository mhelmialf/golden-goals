import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('essentials', 'Football Essentials'),   # bola, sepatu, sarung tangan kiper
        ('apparel', 'Apparel & Jerseys'),        # jersey, jaket, kaos kaki
        ('accessories', 'Accessories'),          # pelindung kaki, tas, botol, headband
        ('collectibles', 'Lifestyle & Collectibles'),  # scarf, poster, merchandise
        ('training', 'Training & Fitness'),      # cone, mini goal, speed ladder
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    product_views = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()