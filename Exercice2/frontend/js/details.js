window.onload = function () {
  const urlParams = new URLSearchParams(window.location.search);
  const factureId = urlParams.get("id");

  const produitsListe = document.getElementById("produitsListe");
  const totalProduits = document.getElementById("totalProduits");
  const totalPrix = document.getElementById("totalPrix");

  fetch(`http://127.0.0.1:8000/api/factures/${factureId}/`)
    .then((res) => res.json())
    .then((data) => {
      if (!data.produits || data.produits.length === 0) {
        produitsListe.innerHTML = "<p>Aucun produit dans cette facture.</p>";
        totalProduits.textContent = "Nombre total de produits : 0";
        totalPrix.textContent = "Total à payer : 0 €";
        return;
      }

      produitsListe.innerHTML = "";
      data.produits.forEach((p) => {
        const div = document.createElement("div");
        div.className = "produit-ligne";
        div.innerHTML = `
                    <span class="nom">${p.nom}</span>
                    <span class="quantite">${p.quantite} x ${p.prix.toFixed(2)} €</span>
                    <span class="total">${p.total.toFixed(2)} €</span>
                `;
        produitsListe.appendChild(div);
      });

      totalProduits.textContent = `Nombre total de produits : ${data.total_produits}`;
      totalPrix.textContent = `Total à payer : ${data.total_prix.toFixed(2)} €`;
    })
    .catch((err) => console.error("Erreur fetch détail facture:", err));
};
