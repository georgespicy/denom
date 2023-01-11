from django.db import models

# Create your models here.

class Subcriber(models.Model):
    email = models.EmailField(max_length=50)
    date_subscribed = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    phone_number = models.PositiveIntegerField(blank=False)
    message = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.first_name