function relojito() {
    hora_actual = new Date()
    hora = hora_actual.getHours()
    minutos = hora_actual.getMinutes()
    segundos = hora_actual.getSeconds()

    imprimeHora = hora + ":" + minutos + ":" + segundos
    document.form_reloj.reloj.value = imprimeHora
    setTimeout("relojito()", 1000)
  }