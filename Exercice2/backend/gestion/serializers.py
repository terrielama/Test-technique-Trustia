from rest_framework import serializers
from .models import Produit, Facture, DetailFacture

# ----- Produit -----
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

# ----- DetailFacture  -----
class DetailFactureSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = DetailFacture
        fields = ['id', 'produit', 'quantite', 'total']

    def get_total(self, obj):
        return round(obj.produit.prix * obj.quantite, 2)

# ----- Facture -----
class FactureSerializer(serializers.ModelSerializer):
    details = DetailFactureSerializer(source='details', many=True, read_only=True) 
    total_facture = serializers.SerializerMethodField()
    total_quantite = serializers.SerializerMethodField()

    class Meta:
        model = Facture
        fields = ['id', 'date_creation', 'details', 'total_quantite', 'total_facture']

    def get_total_facture(self, obj):
        return round(sum(d.produit.prix * d.quantite for d in obj.details.all()), 2)

    def get_total_quantite(self, obj):
        return sum(d.quantite for d in obj.details.all())