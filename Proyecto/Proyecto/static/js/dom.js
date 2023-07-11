function muestraInfo() {
    var elemento = document.getElementById("adicional");
    elemento.className = "visible";
    var enlace = document.getElementById("enlace");
    enlace.className = "oculto";
  }

  function muestraOculta() {
    var obtenido = document.getElementById('contenido');
    var link = document.getElementById('link');
  
    if(obtenido.style.display == "" || obtenido.style.display == "block") {
      obtenido.style.display = "none";
      link.innerHTML = 'Mostrar contenido';
    }
    else {
      obtenido.style.display = "block";
      link.innerHTML = 'Ocultar contenido';
    }
  }




