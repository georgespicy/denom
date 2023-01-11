from django.db import models

# Create your models here.

class Subcriber(models.Model):
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return self.email