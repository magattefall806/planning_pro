from django.db import models


class Departement(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)
    localisation = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Metier(models.Model):
    code = models.CharField(max_length=25, null=True)
    nom = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    departement = models.ForeignKey(Departement, related_name='metiers', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
