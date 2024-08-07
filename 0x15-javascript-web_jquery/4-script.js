
// this will Add a click event listener to the DIV with id 'toggle_header'
// this will Get the current class of the HEADER element
// TO Toggle the class based on the current class

$('div#toggle_header').click(function () {
    $('header').toggleClass('red').toggleClass('green');
});

