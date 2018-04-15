from django.db import models

# new class here in python
class job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length = 200)
