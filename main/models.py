import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('essentials', 'Football Essentials'),   # bola, sepatu, sarung tangan kiper
        ('apparel', 'Apparel & Jerseys'),        # jersey, jaket, kaos kaki
        ('accessories', 'Accessories'),          # pelindung kaki, tas, botol, headband
        ('collectibles', 'Lifestyle & Collectibles'),  # scarf, poster, merchandise
        ('training', 'Training & Fitness'),      # cone, mini goal, speed ladder
    ]
    
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title