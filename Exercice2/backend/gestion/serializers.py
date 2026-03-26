from rest_framework import serializers
from .models import Produit

# ---------- Sérialiseur API ----------
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'