var displayTheseDates = [];
$(document).ready(function(){

$( "td" ).each(function( index ) {
  displayTheseDates.push($(this).text());
  $(this).remove(); 
  console.log( index + ": " + $( this ).text() );
});
	displayTheseDates.shift();
	displayTheseDates.shift();
	$("table").append("<tr><th>Date</th><th>Time</th></tr>")
	console.log(displayTheseDates)
for(var i = 0; i < (displayTheseDates.length/2) ; i++)
{
	$("table").append("<tr><td>"+displayTheseDates[i]+"</td><td>"+displayTheseDates[i+(displayTheseDates.length/2)]+"</td></tr>")
}

});