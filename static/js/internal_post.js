// Side Nav For Mobile
$(document).ready(function(){
	$('.sidenav').sidenav();
});
        

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.fixed-action-btn');
  var instances = M.FloatingActionButton.init(elems, {
    direction: 'left',
    hoverEnabled: false
  });
});

$(document).ready(function(){
  $('.modal').modal({
    opacity:0.5
  });

});

// Login Form JS
$(document).ready(function(e){
   $('h6').on('click',function(){
      $('.social').stop().slideToggle();
   });
})

