/*
let variable = 1.5;
console.log(typeof(variable));
*/
let d = document.querySelector(".div_borde");
    d.style.fontSize='40px';
    d.style.color = 'tomato';
    d.style.border = 'solid';

function Agranda(){
    let t = document.getElementById("agranda");
    t.style.fontSize='28px';
    t.style.color = '#cecece';
}
function Achica(){
    let t = document.getElementById("agranda");
    t.style.fontSize='18px';
    t.style.color = 'blue';
}
function cobros(){
    let cobro = parseFloat(document.forms["mi_formulario"]["cobro"].value);
    let abono = parseFloat(document.forms["mi_formulario"]["abono"].value);
    
    //console.log(typeof(cobro)+ typeof(abono));
    
    if (cobro !== typeof(number) && abono !== typeof(number) ){
        alert("Datos no validos");
    }

    else {
    let total = cobro - abono;
    let ctotal = document.querySelector(".total");
    ctotal.innerHTML=total;
    }
    //let total = cobro + abono;
    //console.log(total);
    

}

