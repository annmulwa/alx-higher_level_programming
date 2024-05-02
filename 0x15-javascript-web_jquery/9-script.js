// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello

let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data) {
  let hellotext = data.hello;
  $('div#hello').text(hellotext);
});
