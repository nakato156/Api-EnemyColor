window.onload = init;

let inputColor, selectColor, previewEC;

function init(){
    selectColor = document.getElementById("selectColor");
    inputColor = document.getElementById("inputColor")
    previewEC = document.getElementById("previewEC");
    
    changeColor();
    selectColor.addEventListener('click', e => inputColor.click())
    inputColor.addEventListener('change', changeColor)
}
function ColorToHex(color) {
    var hexadecimal = color.toString(16);
    return hexadecimal.length == 1 ? "0" + hexadecimal : hexadecimal;
}

function changeColor(e) {
    let color = inputColor.value
    selectColor.style.background = color;
    color = color.slice(1)

    fetch(`/api/v1/getEnemy?color=${color}`)
    .then(req => req.json())
    .then(res => {
        let color_hex  = "#";
        for(canal in res) color_hex+= ColorToHex(res[canal]);
        previewEC.style.background = color_hex;
        console.log(color_hex)
    })
}