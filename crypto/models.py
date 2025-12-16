from django.db import models

class BitcoinPrice(models.Model):
    # Django automatically creates an 'id' field for us!
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.price} at {self.timestamp}"