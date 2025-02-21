from django.db import models

# Create your models here.
from django.db import models

class Price(models.Model):
    item_name = models.CharField(max_length=255, unique=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    currency = models.CharField(max_length=10)  
    date_updated = models.DateTimeField(auto_now=True)  

    def __str__(self):
      return self.item_name

    def to_dict(self):
        return {
            'id': self.id,
            'item_name': self.item_name,
            'price': str(self.price),
            'currency': self.currency,
            'date_updated': self.date_updated.isoformat(),
        }