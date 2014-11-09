var counter = 0; 

$(document).ready(function(){

$(".banner").animate({margin:"0 auto"}, 500);

});

$( "select" ).one("change",function() {
	var target = ".pill";
	target += event.target.id;
	console.log(target); 
 $(String(target)).animate({position:"absolute",top:"-=150"}, 500);
 	counter+=1; 
});

$("#final").click(function(){
	if(counter==5)
	{
		$("#submission").submit(); 
	}
	else
	{
		event.preventDefault(); 
		alert("You didn't quite fill out everything");
	}
});