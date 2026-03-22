import textwrap

# --------------- Dictionnaire ---------------------

phrases = {
    "bloc_1": "Le code propre facilite la maintenance",  # Bloc 1
    "bloc_2": [  # Bloc 2
        "Tester souvent évite beaucoup d erreurs",
        "Cette phrase ne doit pas s afficher"
    ],
    "bloc_3": [  # Bloc 3
        "Cette phrase ne doit pas s afficher",
        "Un bon code doit rester simple et clair",
        "La simplicité améliore la qualité du code",
        "Refactoriser améliore la compréhension"
    ]
}

# -------------------- Blocs -----------------------

ordre_blocs = [
    ["bloc_1"],
    ["bloc_2"],
    ["bloc_3"]
]

# ----------------- Phrases à ne pas afficher -------------

# pas_affiche = [
#     "Cette phrase ne doit pas s afficher", #phrase du bloc 2
#     "Un bon code doit rester simple et clair", #phrase du bloc 3
# ]

phrases_cachees = {
    "bloc_2": ["Cette phrase ne doit pas s afficher"],  
    "bloc_3": ["Un bon code doit rester simple et clair"]  
}


# --------- Fonction : Afficher un bloc ---------

# Boucle : parcourir toutes les phrases du bloc
# Condition : si une phrase est une liste (plusieurs lignes), parcourir chaque ligne
# Condition : si aucune phrase à afficher, sortir de la fonction
# Calculer la longueur max des phrases (limite 100 caractères)
# Afficher le cadre avec '-' pour les lignes et '|' pour les côtés


# Problème rencontré : une même phrase présente dans plusieurs blocs mais doit s'afficher seulement dans un bloc
# Solution : lier les phrases à ne pas afficher à l'ID du bloc correspondant

def afficher_bloc(id_bloc, liste, largeur_max=100):
    lignes = []

    phrases_sautées = phrases_cachees.get(id_bloc, [])

    for phrase in liste:
        if isinstance(phrase, list):
            for ligne in phrase:
                texte = ligne.lower()
                if texte not in [p.lower() for p in phrases_sautées]:
                    lignes.extend(textwrap.wrap(texte, largeur_max))
        else:
            texte = phrase.lower()
            if texte not in [p.lower() for p in phrases_sautées]:
                lignes.extend(textwrap.wrap(texte, largeur_max))

    if not lignes:
        return  

    largeur_bloc = min(max(len(l) for l in lignes), largeur_max)

    print("-" * (largeur_bloc + 4))
    for ligne in lignes:
        print("| " + ligne.ljust(largeur_bloc) + " |")
    print("-" * (largeur_bloc + 4))


# --------- Boucle: Affiche bloc dans l'ordre ---------

for bloc in ordre_blocs:
    for id_phrase in bloc:
        liste = phrases[id_phrase] if isinstance(phrases[id_phrase], list) else [phrases[id_phrase]]
        afficher_bloc(id_phrase, liste)
    print()