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

# ---------- Modèle Facture ----------
# Objectif : calculer le total de la facture et le total des produits

class Facture(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)

    def total_facture(self):
        total = sum(item.produit.prix * item.quantite for item in self.details.all())
        return total

    def total_produits(self):
        return sum(item.quantite for item in self.details.all())


#--- Modèle Détail d'une Facture  ---
# Objectif : représenter les détails d'une facture (produit + quantité)

class DetailFacture(models.Model):
    facture = models.ForeignKey(Facture, related_name='details', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def total(self):
        return round(self.produit.prix * self.quantite, 2)

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite} = {self.total()} €"