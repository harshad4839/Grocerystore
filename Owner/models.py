from django.db import models

class Menu(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description=models.CharField(max_length=300)
    manufacturedate = models.DateField(null=True)
    expirydate = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name