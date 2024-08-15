$(document).ready(function () {
  const list = $('ul.my_list');
  const addItemBtn = $('div#add_item');

  addItemBtn.on('click', function () {
    list.append('<li>Item</li>');
  });
});
