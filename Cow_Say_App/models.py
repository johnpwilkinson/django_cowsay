from django.db import models

# Create your models here.


class Cow_Say_What_Model(models.Model):
    message = models.CharField(max_length=80)
    cow_output = models.TextField(default="")
    

    def __str__(self):
        return self.message