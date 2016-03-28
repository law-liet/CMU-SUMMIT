

  var handler = StripeCheckout.configure({
    key: 'pk_test_bAlcI6gMnSDwQqsfIG6NBf1m',
    //image: '/img/documentation/checkout/marketplace.png',
    locale: 'auto',
    token: function(token) {
      


    }
  });

$('#StripePayButton').on('click', function(e) {
    // Open Checkout with further options

    var a = document.getElementById('NetworkingLunchEvent').checked;
    var b = document.getElementById('PrivateDinner').checked;
    var c = document.getElementById('LunchEvent').checked; 
    var money = 0;
    if (b ==true) {
      money+= 70;
    }

    if (c == true){
      money += 30;
    }
    handler.open({
      name: 'CMU-SUMMIT',
      description: '',
      amount: money
    });
    e.preventDefault();
});

  $(window).on('popstate', function() {
    handler.close();
  });

