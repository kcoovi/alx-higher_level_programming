// JavaScript script which updates the text color of the <header> element
// to red (#FF0000) when user clicked  on the tag DIV#red_header:
const $ = window.$;
$('#red_header').bind('click', function () {
  $('header').css({ color: '#FF0000' });
});
