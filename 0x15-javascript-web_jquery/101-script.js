$(document).ready(function () {
  const list = $('ul.my_list');
  const addItemBtn = $('div#add_item');
  const removeLastItemBtn = $('div#remove_item');
  const clearListBtn = $('div#clear_list');

  addItemBtn.on('click', function () {
    list.append('<li>Item</li>');
  });

  removeLastItemBtn.on('click', function () {
    list.children('li').last().remove();
  });

  clearListBtn.on('click', function () {
    list.empty();
  });
});
