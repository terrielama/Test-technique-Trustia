from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produit, Facture, DetailFacture
from .serializers import ProduitSerializer
from django.core.paginator import Paginator

# ---------- Gestion des produits via API ----------

# ----- Créer nouveau produit -----
# Objectif : enregistrer produit dans bdd + le renvoyer 

@api_view(["POST"])
def creer_produit(request):
    serializer = ProduitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----- Modifier produit existant -----
# Objectif : maj un produit existant

@api_view(["PUT"])
def modifier_produit(request, id):
    try:
        produit = Produit.objects.get(id=id)
    except Produit.DoesNotExist:
        return Response({"error": "Produit non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProduitSerializer(produit, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----- Supprimer produit -----
# Objectif : supprimer produit de la bdd

@api_view(["DELETE"])
def supprimer_produit(request, id):
    try:
        produit = Produit.objects.get(id=id)
    except Produit.DoesNotExist:
        return Response({"error": "Produit non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    produit.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ----- Afficher liste produits + pagination -----
# Objectif : trier par id + afficher liste avec 5 produits par page + pagination

@api_view(["GET"])
def liste_produits(request):
    try:
        produits = Produit.objects.all().order_by('id')

        # Pagination
        page_number = request.GET.get('page', 1)
        paginator = Paginator(produits, 5)
        page = paginator.get_page(page_number)

        serializer = ProduitSerializer(page.object_list, many=True)
        return Response({
            "produits": serializer.data,
            "page": page.number,
            "total_pages": paginator.num_pages
        })
    except Exception as e:
        # Retourne l'erreur pour debug
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# ----------------------- Facturation -----------------------
# ----- Créer facture -----
# Objectif : créer une facture avec plusieurs produits + quantités

@api_view(["POST"])
def creer_facture(request):
    data = request.data

    if "produits" not in data:
        return Response({"error": "Liste produits manquante"}, status=400)

    facture = Facture.objects.create()

    for item in data["produits"]:
        produit_id = item.get("produit_id")
        quantite = item.get("quantite")

        if not produit_id or not quantite:
            return Response({"error": "Données invalides"}, status=400)

        try:
            produit = Produit.objects.get(id=produit_id)
        except Produit.DoesNotExist:
            return Response({"error": f"Produit {produit_id} introuvable"}, status=404)

        DetailFacture.objects.create(
            facture=facture,
            produit=produit,
            quantite=quantite
        )

    return Response({
        "message": "Facture créée",
        "facture_id": facture.id
    }, status=201)


# ----- Détail facture -----
# Objectif : afficher produits + total + nombre

@api_view(["GET"])
def detail_facture(request, id):
    facture = Facture.objects.get(id=id)

    details = facture.details.all()  


    