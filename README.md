# Test-technique - Trustia

# Exercice 1 -- Blocs de texte en Python

## Description

Ce programme Python affiche dans la console des blocs de texte avec un
encadrement.

Chaque bloc contient une ou plusieurs phrases entourées de : - tirets
(-) pour le haut et le bas - barres verticales (\|) sur les côtés

---

## Règles

- Le texte est affiché en minuscules
- La largeur maximale est de 100 caractères (modifiable)
- Les phrases sont stockées dans un dictionnaire
- Certaines phrases ne sont pas affichées volontairement

---

## Blocs affichés

Bloc 1 : - le code propre facilite la maintenance

Bloc 2 : - tester souvent evite beaucoup d erreurs - Cette phrase ne doit pas s afficher

Bloc 3 : - Cette phrase ne doit pas s afficher - Un bon code doit rester simple et clair - la simplicite ameliore la qualite du code - refactoriser
ameliore la comprehension

---

## Les phrases ne devant pas apparaître dans la console

Bloc 2 : « Cette phrase ne doit pas s afficher »

## Bloc 3 : « Un bon code doit rester simple et clair »

## Important

Ces phrases ne doivent jamais être affichées : - cette phrase ne doit
pas s afficher - un bon code doit rester simple et clair

---

## Objectif

Le programme permet facilement : - de modifier le texte - de changer
l'ordre des blocs - d'ajouter ou supprimer des lignes - de garder des
phrases sans les afficher

---

## Lancer le programme

python main.py

---

Exercice 2 : Créer une application web Django permettant de gérer des produits et de générer des factures.

# Application de Gestion de Produits & Facturation

## Description

Cette application web développée avec Django (backend) et JavaScript
(frontend) permet de :

- Gérer des produits (CRUD)
- Créer des factures avec plusieurs produits
- Définir des quantités
- Consulter le détail d'une facture

---

## Fonctionnalités

### Gestion des produits

- Créer un produit
- Modifier un produit
- Supprimer un produit
- Afficher la liste des produits
- Pagination des produits

### Facturation

- Créer une facture
- Sélectionner plusieurs produits
- Définir une quantité pour chaque produit

### Détail d'une facture

- Liste des produits
- Quantité x prix unitaire par produit
- Nombre total des produits
- Total à payer (arrondi à 2 décimales)

---

## Interface

- Interface simple
- Liste des produits avec boutons Modifier / Supprimer
- Page "Créer facture" avec défilement pour afficher tous les produits
- Navigation entre les pages (Produits / Factures)

---

## Technologies utilisées

- Backend : Django + Django REST Framework\
- Frontend : HTML, CSS, JavaScript\
- Base de données : SQLite

---

## Installation

1.  Cloner le projet : git clone https://github.com/terrielama/Test-technique-Trustia/tree/main

2.  Aller dans le dossier : cd projet

3.  Créer un environnement virtuel : python -m venv env

4.  Activer l'environnement : env\Scripts\activate

5.  Installer les dépendances : pip install -r requirements.txt

6.  Lancer les migrations : python manage.py migrate

7.  Démarrer le serveur :
    - cd backend
    - python manage.py runserver

## Lancer le front

1.  cd frontend

2.  python -m http.server 5500

---

## Administration Django

L'interface d'administration Django : http://127.0.0.1:8000/admin/

Un superutilisateur (superuser) a été créé pour accéder à cette
interface.

admin
admin

Possibilité de gérer : - les produits - les factures - les détails de
facture

---

## API

### Produits

- GET /produits/
- GET /produits/all/
- POST /produits/creer/
- PUT /produits/modifier/`<id>`/
- DELETE /produits/supprimer/`<id>`/

### Factures

- POST /factures/creer/
- GET /factures/`<id>`/

---

## Objectif

Ce projet permet de comprendre : - le fonctionnement d'une API Django
REST - la gestion de la pagination - les relations entre modèles
(Facture et Produits) - la création d'un frontend simple en JavaScript

> > > > > > > modif_readme
