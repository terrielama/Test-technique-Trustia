from django.db import models

# Create your models here.

#---------- Modèle Produit ----------
# id, nom, prix, date de péremption.
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField()
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom

