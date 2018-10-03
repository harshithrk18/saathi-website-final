
$(".modal").each(function(l){$(this).on("show.bs.modal",function(l){var o=$(this).attr("data-easein");$(".modal-dialog").velocity("transition."+o)})});
// $(window).resize(function() {

//   if ($(this).width() < 500) {

//     $('.member-info-content').hide();
//     $('.member-info-content-mobile').hide();

//   }else if ($(this).width() > 500 ) {

//     $('.member-info-content').hide();
//     $('.member-info-content-mobile').hide();
//     }

// });

if ($(window).width() > 500){
     $('.member-info-content').show();
    $('.member-info-content-mobile').hide();
}

$(window).on('resize', function() {
  var win = $(this);
  if (win.width() < 514) {
    $('.member-info-content').hide();
    $('.member-info-content-mobile').show();


  }else {
    $('.member-info-content').show();
    $('.member-info-content-mobile').hide();
  }

});
