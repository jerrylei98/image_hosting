window.onload = function start(){
  setInterval(show_file, 50);
}


function show_file(){
  var uploaded_file = document.getElementById("file_upload")
  var file_name = uploaded_file.value;
  file_name = file_name.split("\\");
  file_name = file_name[file_name.length - 1];
  document.getElementById("file_name").innerHTML=file_name;
  if (uploaded_file.size > 200){
      console.log("File size must under 2mb!");
  }
}
