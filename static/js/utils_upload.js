window.onload = function start(){
  setInterval(show_file, 1000);
}


function show_file(){
  var file_name = document.getElementById("file_upload").value;
  document.getElementById("file_name").innerHTML=file_name;
}
