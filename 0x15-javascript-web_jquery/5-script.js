//this will  Attach a click event handler to the div with id "add_item"
//this will  Append a new <li> element with the text "Item" to the <ul> with class "my_list"

$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
