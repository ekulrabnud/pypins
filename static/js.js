$(document).on("pagecreate","#pageone",function(){
  $("button").click(function(){
	id = $(this).attr('id')
	id = "#"+id
	pin = $(this).attr('id')
	console.log(id)
	path = "/relay"   
	console.log(path)
$.get(path,{pin:pin},function(data,status){
    console.log(data);	
		if (data == "Off"){
		console.log("true")
		$(id).text("ON");}
		else{$(id).text("OFF");}	
	
    });
  });
});
