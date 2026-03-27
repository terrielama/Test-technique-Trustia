window.onload = function () {
  const produitsContainer = document.getElementById("produitsContainer");

  // ----- Afficher tous les produits avec champ quantité -----
  function fetchProduits() {
    fetch("http://127.0.0.1:8000/api/produits/")
      .then((res) => res.json())
      .then((data) => {
        if (!data.produits || data.produits.length === 0) {
          produitsContainer.innerHTML = "<p>Aucun produit disponible.</p>";
          return;
        }

        produitsContainer.innerHTML = ""; // vider le conteneur

        data.produits.forEach((p) => {
          const div = document.createElement("div");
          div.className = "produit-facture";
          div.innerHTML = `
            <span><b>${p.nom}</b> - ${p.prix.toFixed(2)} €</span>
            <input type="number" min="0" value="0" data-id="${p.id}" class="quantite" style="width:60px; margin-left:10px;">
          `;
          produitsContainer.appendChild(div);
        });
      })
      .catch((err) => console.error("Erreur fetchProduits:", err));
  }

  // ----- Créer une facture -----
  document
    .getElementById("factureForm")
    .addEventListener("submit", function (e) {
      e.preventDefault();

      const quantites = document.querySelectorAll(".quantite");
      const produits = [];

      quantites.forEach((q) => {
        const qty = parseInt(q.value);
        if (qty > 0) {
          produits.push({ produit_id: q.dataset.id, quantite: qty });
        }
      });

      if (produits.length === 0) {
        alert("Sélectionnez au moins un produit avec une quantité > 0");
        return;
      }

      fetch("http://127.0.0.1:8000/api/factures/creer/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ produits }),
      })
        .then((res) => res.json())
        .then((data) => {
          alert(`Facture créée ! ID: ${data.facture_id}`);
          document.getElementById("factureForm").reset();

          // Rediriger vers la liste des factures
          window.location.href = "liste_factures.html";
        })
        .catch((err) => console.error("Erreur création facture:", err));
    });

  // Initialisation
  fetchProduits();
};
