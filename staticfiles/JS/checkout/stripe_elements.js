
//contents of this take from from strip ci: Project - Boutique Ado  Setting Up Payments  Integrating Stripe Elements for Secure Card Input
// https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+7/courseware/eb05f06e62c64ac89823cc956fcd8191/97568b525c8b4387924451f8c7353ef6/?child=first


/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '18px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
var controlSubmit = document.getElementById('submit-button')
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
      if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
        controlSubmit.disabled = true;
    } else {
        errorDiv.textContent = '';
         controlSubmit.disabled = false;
    }

});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name:$.trim(form.billing_name.value),
                phone:$.trim(form.phone.value),
                address:{
                    line1:$.trim(form.address_line_1.value),
                    line2:$.trim(form.address_line_2.value),
                    city:$.trim(form.town.value),
                    postal_code:$.trim(form.postcode.value),
                },
            email:$.trim(form.email.value),
            }
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});

document.addEventListener("DOMContentLoaded", (event) => {
     controlSubmit.disabled = true;
  });