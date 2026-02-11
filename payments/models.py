from django.db import models

# Create your models here.
class Transaction(models.Model):
    reference = models.CharField(max_length=100)
    amount = models.FloatField()
    currency = models.CharField(max_length=10)
    fee = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference