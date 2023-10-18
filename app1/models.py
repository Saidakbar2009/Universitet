from django.db import models

# Create your models here.
class Yonalish(models.Model):
    nom = models.CharField(max_length=50)
    aktiv = models.BooleanField()
    def __str__(self):
        return self.nom
class Fan(models.Model):
    nom = models.CharField(max_length=50)
    yonalish= models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField()
class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=10)
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=20)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)