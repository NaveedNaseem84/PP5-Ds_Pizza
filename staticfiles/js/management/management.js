const deleteButtons = document.getElementsByClassName("btn-delete-booking");
const deleteConfirm = document.getElementById("deleteConfirmation");

let productId = null;
let productType = null;

document.addEventListener("DOMContentLoaded", domEventListener);

function domEventListener() {

   for (let button of deleteButtons) {
    button.addEventListener("click", processProductDelete);     
  }

}

function processProductDelete() {
   productId = this.getAttribute("data-product-id");
   productType = this.getAttribute("data-product-type");
  
  deleteConfirm.addEventListener("click", () => {
     if (productId && productType) {
      window.location.href = `delete_product/${productId}/?item_type=${productType}`;   
     }
  });
}


