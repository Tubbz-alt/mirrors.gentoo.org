//Add more fields dynamically.
function addField(area,field,limit) {
if(!document.getElementById) return; //Prevent older browsers from getting any further.
var field_area = document.getElementById(area);
var all_inputs = field_area.getElementsByTagName("input"); //Get all the input fields in the given area.
//Find the count of the last element of the list. It will be in the format '<field><number>'. If the
// field given in the argument is 'friend_' the last id will be 'friend_4'.
var last_item = all_inputs.length - 1;
var last = all_inputs[last_item].id;
var count = Number(last.split("_")[1]) + 1;
     
//If the maximum number of elements have been reached, exit the function.
// If the given limit is lower than 0, infinite number of fields can be created.
if(count > limit && limit > 0) return;
     
if(document.createElement) { //W3C Dom method.
  var div = document.createElement("div");
  var input = document.createElement("input");
  input.id = field+count;
  input.name = field+count;
  input.type = "text"; //Type of field - can be any valid input type like text,file,checkbox etc.
  div.appendChild(input);
  field_area.appendChild(div);
  } 
else 
  { //Older Method
    field_area.innerHTML += "<input name='"+(field+count)+"' id='"+(field+count)+"' type='text' />";
  }
}
