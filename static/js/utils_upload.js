/*
window.onload = function start(){
  setInterval(show_file, 50);
}


function show_file(){
  var uploaded_file = document.getElementById("file_upload")
  var file_name = uploaded_file.value;
  file_name = file_name.split("\\");
  file_name = file_name[file_name.length - 1];
  document.getElementById("file_name").innerHTML=file_name;
}
*/
var control = document.getElementById("file_upload");
control.addEventListener("change", function(event) {
  var i = 0,
    files = control.files,
    len = files.length;

  var size_check = false;
  var type_check = false;
  for (; i < len; i++) {
    if(files[i].type.indexOf("image/") != -1){ //if filetype is image
      type_check = true;
    }
    else{
      type_check = false;
    }
    if(files[i].size < 5242880){
      size_check = true;
    }
    else{
      size_check = false;
    }
    if(size_check == false){
      var delete_upload = document.getElementById('check_upload_div');
      if(delete_upload != null){
        delete_upload.parentNode.removeChild(delete_upload);
      }
    }
    if(type_check == false){
      var delete_upload = document.getElementById('check_upload_div');
      if(delete_upload != null){
        delete_upload.parentNode.removeChild(delete_upload);
      }
    }
    if(size_check == true && type_check == true){
      var checked_upload = document.createElement("div");
      checked_upload.setAttribute("id", "check_upload_div");
      checked_upload.innerHTML = "<input type='submit' class='checked_upload' value='Upload' name='button' value='upload_button'>";
      document.getElementById("upload_form").appendChild(checked_upload);
    }
    document.getElementById("file_name").innerHTML=files[i].name;
  }

}, false);
