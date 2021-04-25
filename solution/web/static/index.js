$(document).ready(function() {
  $(".hidden").fadeOut();

  var canvas = document.querySelector("canvas");
  var signaturePad = new SignaturePad(canvas);
  signaturePad.on();

  $("#viewfile").click(function() {
    $(".hidden").fadeIn();
  });

  $("#sign").click(function() {
    var signature = signaturePad.toDataURL();

    $.ajax({
      type: "POST",
      url: '/saveSignature',
      data: JSON.stringify({ 'signature': signature }),
      success: () => {
        alert('sent');
      },
      contentType: 'application/json'
    });
  });
});
