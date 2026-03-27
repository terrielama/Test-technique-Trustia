from django.urls import path
from .views import liste_produits, creer_produit, modifier_produit, supprimer_produit, creer_facture, detail_facture, liste_factures

urlpatterns = [
# ----- Gestion des produits -----
    path('produits/', liste_produits, name='liste_produits'),
    path('produits/creer/', creer_produit, name='creer_produit'),
    path('produits/modifier/<int:id>/', modifier_produit, name='modifier_produit'),
    path('produits/supprimer/<int:id>/', supprimer_produit, name='supprimer_produit'),

# ----- Facturation -----
    path("factures/creer/", creer_facture, name='creer_facture'),
    path("factures/<int:id>/", detail_facture, name='detail_facture'),
    path("factures/", liste_factures, name='liste_factures'),
]