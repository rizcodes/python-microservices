from django.db import models


# Create your models here.
class Dinosaur(models.Model):
    name = models.CharField(max_length=128)
    image = models.CharField(max_length=255)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Dinosaur'
        verbose_name_plural = 'Dinosaurs'

    def __str__(self):
        return self.name
