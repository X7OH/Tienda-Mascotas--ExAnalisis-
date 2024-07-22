function habilitarEdicion() {
    document.getElementById('btnEditar').style.display = 'none';
    document.getElementById('btnGuardar').style.display = 'inline-block';
    document.getElementById('btnCancelar').style.display = 'inline-block';
    // Habilitar los campos de formulario aquí si es necesario
}

function cancelarEdicion() {
    document.getElementById('btnEditar').style.display = 'inline-block';
    document.getElementById('btnGuardar').style.display = 'none';
    document.getElementById('btnCancelar').style.display = 'none';
    // Deshabilitar los campos de formulario aquí si es necesario
}