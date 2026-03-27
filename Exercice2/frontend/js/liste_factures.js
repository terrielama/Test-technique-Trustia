function loadFactures() {
  fetch("http://127.0.0.1:8000/api/factures/")
    .then((res) => res.json())
    .then((data) => {
      const container = document.getElementById("facturesContainer");
      container.innerHTML = "";

      if (data.length === 0) {
        container.innerHTML = "<p>Aucune facture</p>";
        return;
      }

      data.forEach((f) => {
        const div = document.createElement("div");
        div.className = "produit";

        div.innerHTML = `
          <span><b>Facture #${f.id}</b></span><br>
          <span>${new Date(f.date).toLocaleString()}</span><br>
          <a href="details.html?id=${f.id}">Voir détail</a>
        `;

        container.appendChild(div);
      });
    });
}

loadFactures();
