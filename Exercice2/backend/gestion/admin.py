from django.contrib import admin
from .models import Produit, Facture, DetailFacture

# Inline pour afficher les details directement dans la facture
class DetailFactureInline(admin.TabularInline):
    model = DetailFacture
    extra = 1  # nombre de details vides supplémentaires
    readonly_fields = ('total',)

class FactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_creation', 'total_facture')
    inlines = [DetailFactureInline]

    # Calculer le total de la facture
    def total_facture(self, obj):
        return round(sum(l.total() for l in obj.details.all()), 2)
    total_facture.short_description = "Total €"

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prix', 'date_peremption')
    list_filter = ('date_peremption',)
    search_fields = ('nom',)

admin.site.register(Produit, ProduitAdmin)
admin.site.register(Facture, FactureAdmin)