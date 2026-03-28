window.onload = function () {
  // Variables globales pour pagination
  let currentPage = 1;
  let totalPages = 1;

  const container = document.getElementById("produitsContainer");

  // ----- Afficher les produits + pagination -----
  function fetchProduits(page = 1) {
    fetch(`http://127.0.0.1:8000/api/produits/?page=${page}`)
      .then((res) => res.json())
      .then((data) => {
        totalPages = data.total_pages;
        currentPage = data.page;

        container.innerHTML = ""; // vide le conteneur avant d'afficher

        if (data.produits.length === 0) {
          container.innerHTML = "<p>Aucun produit disponible.</p>";
        } else {
          data.produits.forEach((p) => {
            const div = document.createElement("div");
            div.className = "produit";
            div.innerHTML = `
              <span><b>ID:</b> ${p.id}</span>
              <span><b>Nom du produit :</b> ${p.nom}</span>
              <span><b>Prix:</b> ${p.prix} €</span>
              <span><b>A consommer avant le :</b> ${p.date_peremption}</span>
              <div>
                <button class="modifier" onclick="editProduit(${p.id}, '${p.nom}', ${p.prix}, '${p.date_peremption}')">Modifier</button>
                <button class="supprimer" onclick="deleteProduit(${p.id})">Supprimer</button>
              </div>
            `;
            container.appendChild(div);
          });
        }

        document.getElementById("currentPage").innerText = currentPage;
      })
      .catch((err) => console.error("Erreur fetchProduits:", err));
  }

  // ----- Créer ou modifier produit -----
  document
    .getElementById("produitForm")
    .addEventListener("submit", function (e) {
      e.preventDefault();

      const id = document.getElementById("produitId").value;
      const nom = document.getElementById("nom").value.trim();
      const prix = parseFloat(document.getElementById("prix").value);
      const date_peremption = document.getElementById("date_peremption").value;

      if (!nom || !prix || !date_peremption) {
        alert("Tous les champs sont obligatoires !");
        return;
      }

      const url = id
        ? `http://127.0.0.1:8000/api/produits/modifier/${id}/`
        : "http://127.0.0.1:8000/api/produits/creer/";
      const method = id ? "PUT" : "POST";

      fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nom, prix, date_peremption }),
      })
        .then((res) => res.json())
        .then(() => {
          document.getElementById("produitForm").reset();
          document.getElementById("produitId").value = "";
          currentPage = 1;
          fetchProduits(currentPage);
        })
        .catch((err) => console.error("Erreur création/modification:", err));
    });

  // ----- Pré-remplir form pour modification -----
  window.editProduit = function (id, nom, prix, date_peremption) {
    document.getElementById("produitId").value = id;
    document.getElementById("nom").value = nom;
    document.getElementById("prix").value = prix;
    document.getElementById("date_peremption").value = date_peremption;
  };

  // ----- Supprimer un produit -----
  window.deleteProduit = function (id) {
    if (!confirm("Voulez-vous vraiment supprimer ce produit ?")) return;

    fetch(`http://127.0.0.1:8000/api/produits/supprimer/${id}/`, {
      method: "DELETE",
    })
      .then((res) => {
        if (res.status !== 204) throw new Error("Erreur suppression produit");
        fetchProduits(currentPage);
      })
      .catch((err) => console.error("Erreur suppression:", err));
  };

  // ----- Pagination -----
  document.getElementById("prevPage").addEventListener("click", () => {
    if (currentPage > 1) {
      currentPage--;
      fetchProduits(currentPage);
    }
  });

  document.getElementById("nextPage").addEventListener("click", () => {
    if (currentPage < totalPages) {
      currentPage++;
      fetchProduits(currentPage);
    }
  });

  // ----- Initialisation -----
  fetchProduits(currentPage);
};
