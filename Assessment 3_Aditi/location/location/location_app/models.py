from django.db import models
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
   

    def __str__(self):
        return f"{self.name}, {self.city}"
