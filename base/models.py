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

    def __str__(self):
        formatted_date = self.date.strftime("%d/%m/%Y %H:%M")
        return f'{self.name} - {self.food} - {self.pay} - {formatted_date}'

class RabbiOrderBurgers(models.Model):
    count = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)
    is_done = models.BooleanField(default=False)
    
    left = models.PositiveIntegerField(default=count)

    def __str__(self):
        formatted_date = self.date.strftime("%d/%m/%Y %H:%M")
        return f'{self.count} - {formatted_date} ({self.left})'

class RabbiOrderHotdogs(models.Model):
    count = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)
    is_done = models.BooleanField(default=False)
    
    left = models.PositiveIntegerField(default=count)

    def __str__(self):
        formatted_date = self.date.strftime("%d/%m/%Y %H:%M")
        return f'{self.count} - {formatted_date} ({self.left})'