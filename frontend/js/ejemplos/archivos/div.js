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
    
//2 formas de validar si es un tipo de dato numero
// con la funcion is NaN
    if(isNaN(cobro) && isNaN(abono)){
        alert("Error en los tipos de datos");
    }
    else {
        alert("Datos validos, procesando...");
        let total = cobro - abono;
        let ctotal = document.querySelector(".total");
        document.getElementById('total').value = total
        ctotal.innerHTML=total;
    //let total = cobro + abono;
    //console.log(total);
}

/********************
 * 
 * 
 * lo que se hara con Jquery de forma mas rapida
 == Usos basicos 
 == Mostrar ocultar(hide, show, fadein, fadeout, SlideIn, SlideOut), cambiar colores y textos
 == Validar formularios vacios
 == Shake, Delay estos van con timing
 == BlockUI usos y adornos
 == Sweet Alert (ejemplos de uso)
 == Alertify (ejemplos de uso)

 * 
 */


}

