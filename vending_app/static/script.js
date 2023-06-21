// Получаем ссылки на кнопки и элементы счетчика
var plusButtons = document.getElementsByClassName('plus_button');
var minusButtons = document.getElementsByClassName('minus_button');
var countElements = document.getElementsByClassName('count_number count');

// Добавляем обработчики событий для кнопок "+"
for (var i = 0; i < plusButtons.length; i++) {
  plusButtons[i].addEventListener('click', function (event) {
    event.preventDefault();
    var countElement = this.parentNode.querySelector('.count_number.count');
    var count = parseInt(countElement.textContent);
    if (count < 10) {
      countElement.textContent = count + 1;
      updateTotal();
      saveTotal();
    }
  });
}

// Добавляем обработчики событий для кнопок "-"
for (var i = 0; i < minusButtons.length; i++) {
  minusButtons[i].addEventListener('click', function (event) {
    event.preventDefault();
    var countElement = this.parentNode.querySelector('.count_number.count');
    var count = parseInt(countElement.textContent);
    if (count > 0) {
      countElement.textContent = count - 1;
      updateTotal();
      saveTotal();
    }
  });
}

// Обновляем общую сумму
function updateTotal() {
  var counts = document.querySelectorAll('.count_number.count');
  var prices = document.querySelectorAll('.price.price_per_item');
  var total = 0;

  for (var i = 0; i < counts.length; i++) {
    var count = parseInt(counts[i].textContent);
    var price = parseInt(prices[i].textContent);
    total += count * price;
  }

  var totalElement = document.getElementById('totalAmount');
  totalElement.textContent = 'Total: ' + total + '֏';
}

// Сохраняем общую сумму в localStorage
function saveTotal() {
  var totalElement = document.getElementById('totalAmount');
  var totalValue = totalElement.textContent;
  localStorage.setItem('totalAmount', totalValue);
}

// Загружаем сохраненную общую сумму из localStorage
function loadTotal() {
  var totalValue = localStorage.getItem('totalAmount');
  if (totalValue) {
    var totalElement = document.getElementById('totalAmount');
    totalElement.textContent = totalValue;
  }
}

// Загружаем сохраненную общую сумму при загрузке страницы
loadTotal();
