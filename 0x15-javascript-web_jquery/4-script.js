$(document).ready(function () {
  const header = $('header');

  $('DIV#toggle_header').click(function () {
    header.toggleClass('green red orange');

    // if (header.hasClass('red')){
    //    header.removeClass('red');
    //    header.addClass('green');
    // }else{
    //    header.removeClass('green');
    //    header.addClass('red');
    // }
  });
});
