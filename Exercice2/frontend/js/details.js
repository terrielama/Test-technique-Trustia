const params = new URLSearchParams(window.location.search);
const id = params.get("id");

fetch(`http://127.0.0.1:8000/api/factures/${id}/`)
  .then((res) => res.json())
  .then((data) => {
    const container = document.getElementById("factureContainer");

    container.innerHTML = `<h2>Facture #${data.facture_id}</h2>`;

    data.produits.forEach((p) => {
      container.innerHTML += `
        <div class="produit">
          Nom du produit: ${p.nom}<br>
          Prix: ${p.prix} € <br>
          Quantité: ${p.quantite}<br>
          Prix x quantité : ${p.total} €
        </div>
      `;
    });

    container.innerHTML += `
      <h3>Nombre total de produits : ${data.total_produits}</h3>
      <h3>Total à payer : ${data.total_prix} €</h3>
    `;
  });
