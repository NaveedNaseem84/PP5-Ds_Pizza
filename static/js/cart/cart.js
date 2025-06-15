const increaseBtn = document.getElementsByClassName("btn-increase-quantity");
const decreaseBtn = document.getElementsByClassName("btn-reduce-quantity");

document.addEventListener("DOMContentLoaded", domEventListener);

function domEventListener() {

   for (let button of increaseBtn) {
    button.addEventListener("click", IncreaseCartQty);     
  }

   for (let button of decreaseBtn) {
    button.addEventListener("click", DecreaseCartQty);     
  }
}

function IncreaseCartQty() {

  let itemId = this.getAttribute("data-item-id");
  let itemType = this.getAttribute("data-item-type");
  if (itemId && itemType) {
    window.location.href = `increase/${itemId}/${itemType}`;

    }
}

function DecreaseCartQty() {

  let itemId = this.getAttribute("data-item-id");
  let itemType = this.getAttribute("data-item-type");
  if (itemId && itemType) {
    window.location.href = `decrease/${itemId}/${itemType}`;

    }
}