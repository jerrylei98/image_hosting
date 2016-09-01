/**
 * Checks if the div is style is block or none. Switches to the other one.
 *
 * divName: The id of the div that is to be switched.
 *
 */
function showHideDiv(divName){
  if (document.getElementById(divName).style.display == "none"){document.getElementById(divName).style.display = "block";}
  else{document.getElementById(divName).style.display = "none";}
}

/**
 *
 * Sole purpose of this function is to switch between login/signup on login/signup page
 *
*/

function login_signup(divName, divName2, formDiv,formDiv2){
  //not selected denoted by black color
  document.getElementById(divName).style.color = "green";
  document.getElementById(divName2).style.color = "black";

  //form change
  document.getElementById(formDiv).style.display = "block";
  document.getElementById(formDiv2).style.display = "none";
}


/////////////////////
