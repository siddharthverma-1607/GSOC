var PythonShell = require("python-shell")
var path = require("path")

function get_userData() {
 
 var queries = document.getElementById("queries").value
 var email =  document.getElementById("email").value

 
 var options = {
    mode : 'text',
    encoding : 'utf8',
    pythonOptions : ['-u'], 
    scriptPath : '/Users/macair/Desktop/Siddharth/Final year project/GSOC/engine',
    args : [queries],
    pythonPath : '/Users/macair/opt/anaconda3/bin/python'
 }

 let userData = new python('userData_toDb.py', options);

 userData.on('message', function(message){
     console.write(message);
 })
 document.getElementById("queries").value = "";
 document.getElementById("email").value = "";

}