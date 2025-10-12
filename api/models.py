import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User:
    pass

class Product(models.Model):
    name=models.TextField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to='products/',blank=True,null=True)

    @property
    def in_stock(self):
        return self.stock>0

    def __str__(self):
        return self.name
    
class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
