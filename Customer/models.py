from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    totalprice=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40, null=True, blank=True)

    user_type_options = (
        ("customer", "customer"),
        ("admin", "admin"),
    )
    user_type = models.CharField(
        max_length=20,
        choices=user_type_options,
        default='customer'
    )

    primary_phone = models.CharField(max_length=40, null=True, blank=True)
    name = models.CharField(max_length=40,null=True,blank=True)
    active_status = models.BooleanField(default=True)
    enabled_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', 'id']