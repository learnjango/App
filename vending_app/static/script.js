var plusButtons = document.getElementsByClassName('plus_button');
var minusButtons = document.getElementsByClassName('minus_button');
var countElements = document.getElementsByClassName('count_number count');

for (var i = 0; i < plusButtons.length; i++) {
  plusButtons[i].addEventListener('click', function (event) {
    event.preventDefault();
    var countElement = this.parentNode.querySelector('.count_number.count');
    var count = parseInt(countElement.textContent);
    if (count < 10) {
      countElement.textContent = count + 1;
      updateTotal();
    }
  });
}

for (var i = 0; i < minusButtons.length; i++) {
  minusButtons[i].addEventListener('click', function (event) {
    event.preventDefault();
    var countElement = this.parentNode.querySelector('.count_number.count');
    var count = parseInt(countElement.textContent);
    if (count > 0) {
      countElement.textContent = count - 1;
      updateTotal();
    }
  });
}

function updateTotal() {
  var counts = document.querySelectorAll('.count_number.count');
  var prices = document.querySelectorAll('.price.price_per_item');
  var total = 0;

  for (var i = 0; i < counts.length; i++) {
    var count = parseInt(counts[i].textContent);
    var price = parseInt(prices[i].textContent);
    total += count * price;
  }

  localStorage.setItem('total', total.toString());

  var totalElement = document.getElementById('totalAmount');
  totalElement.textContent = 'Total: ' + total + '֏';
}

var savedTotal = localStorage.getItem('total');

if (savedTotal !== null) {
  var total = parseInt(savedTotal);

  var totalElement = document.getElementById('totalAmount');
  totalElement.textContent = 'Total: ' + total + '֏';
}
