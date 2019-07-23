from django.db import models

class Restaurant(models.Model):
    name =models.CharField(max_length=20)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name




