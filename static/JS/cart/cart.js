const increaseBtn = document.getElementsByClassName("btn-increase-quantity");

document.addEventListener("DOMContentLoaded", domEventListener);

function domEventListener() {

   for (let button of increaseBtn) {
    button.addEventListener("click", IncreaseCartQty);     
  }
}

function IncreaseCartQty() {

  let itemId = this.getAttribute("data-item-id");
  let itemType = this.getAttribute("data-item-type")
  if (itemId && itemType) {
    window.location.href = `increase/${itemId}/${itemType}`;

    }
}