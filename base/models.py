from django.db import models
from django.utils import timezone

class Order(models.Model):
    FOOD_CHOICES = (
        ('BURGER', 'המבורגר'),
        ('HOTDOG', 'נקנקיה'),
        ('TOAST', 'סודוך'),
    )

    PAY_CHOICES = (
        ('CASH', 'מזומן'),
        ('NOTE', 'שוברים'),
    )

    name = models.CharField(max_length=100)
    food = models.CharField(max_length=100, choices=FOOD_CHOICES)
    pay = models.CharField(max_length=100, choices=PAY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

class RabbiOrder(models.Model):
    burgers = models.PositiveIntegerField()
    hotdogs = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)
    is_done = models.BooleanField(default=False)
    
    burgers_left = models.PositiveIntegerField(default=burgers)
    hotdogs_left = models.PositiveIntegerField(default=hotdogs)