from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_emissions = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username

class EmissionFactor(models.Model):
    category = models.CharField(max_length=100)  # e.g., transport
    activity = models.CharField(max_length=100)  # e.g., car, bus, beef
    unit = models.CharField(max_length=100)      # e.g., km, kg, kWh
    factor = models.FloatField()  # CO₂ emission per unit (kg CO₂/unit)

    def __str__(self):
        return f"{self.category} - {self.activity}"

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)  # e.g., transport, food
    activity = models.CharField(max_length=100)  # e.g., car
    unit = models.FloatField()                   # e.g., 10 km
    emission = models.FloatField()               # calculated CO₂
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity} - {self.date}"

