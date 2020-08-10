
//bring in electron
const electron = require('electron');
//bring in core node.js modules
const url = require('url');
const path = require('path');

//get main window render process creation stuff from electon
const{app, BrowserWindow} = electron;

/*create variable to represent the main window
listen for the app to be ready and run the main function*/

let mainWndow;

app.on('ready', function(){
    //function to create new window
    mainWindow = new BrowserWindow({width:1150, height:650, frame:false});
    //load HTML file into windwow
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'mainwindow.html'),
        protocol: 'file:',
        
    }));
    mainWindow.setMenu(null);
});
var btnContainer = document.getElementsByClassName("menu2");

var btns = btnContainer.getElementsByClassName("tablinks");

for(var i = 0; 1< btns.length; i++){
    btns[i].addEventListener("click", function(){
        var current = document.getElementsByClassName("active");
        if(current.length > 0){
            current[0].className = current.className.replace("active", "");
        }
        this.className += " active";
    });
}

var import_export_area, calculate_area, data_area, settings_area;
function import_tab(){
    import_export_area = document.getElementById("import_export_area");
    import_export_area.style.display = "block";
    calculate_area = document.getElementById("calculate_area");
    calculate_area.style.display = "none";
    data_area = document.getElementById("data_area");
    data_area.style.display = "none";
    settings_area = document.getElementById("settings_area");
    settings_area.style.display = "none";
    evt.import.tablinks += "active"
    
}
function calculate_tab(){
    import_export_area = document.getElementById("import_export_area");
    import_export_area.style.display = "none";
    calculate_area = document.getElementById("calculate_area");
    calculate_area.style.display = "block";
    import_export_area = document.getElementById("data_area");
    import_export_area.style.display = "none";
    import_export_area = document.getElementById("settings_area");
    import_export_area.style.display = "none";
}
function data_tab(){
    import_export_area = document.getElementById("import_export_area");
    import_export_area.style.display = "none";
    import_export_area = document.getElementById("calculate_area");
    import_export_area.style.display = "none";
    import_export_area = document.getElementById("data_area");
    import_export_area.style.display = "block";
    import_export_area = document.getElementById("settings_area");
    import_export_area.style.display = "none";
}
function settings_tab(){
    import_export_area = document.getElementById("import_export_area");
    import_export_area.style.display = "none";
    import_export_area = document.getElementById("calculate_area");
    import_export_area.style.display = "none";
    import_export_area = document.getElementById("data_area");
    import_export_area.style.display = "none";
    import_export_area = document.getElementById("settings_area");
    import_export_area.style.display = "block";
}
var btnContainer = document.getElementsByClassName("menu2");

var btns = btnContainer.getElementsByClassName("tablinks");

for(var i = 0; 1< btns.length; i++){
    btns[i].addEventListener("click", function(){
        var current = document.getElementsByClassName("active");
        if(current.length > 0){
          current[0].className = current.className.replace("active", "");
        }
        this.className += " active";
    });
}
    document.addEventListener("DOMContentLoaded", () => {loadData(); });

