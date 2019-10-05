$("#slim_container").slim({
    ratio: '1:1',
    //service: '/',
    //download: false,
    maxFileSize: 1,
    //willSave: function(data, ready) {
    //  ready(data)
    //},

    label:'Foto de tu mascota aqui',
    buttonConfirmLabel: 'Listo',
    buttonCancelLabel: 'Cancelar',
    buttonEditLabel: 'Editar',
    buttonRemoveLabel: 'Eliminar',
    statusFileType:`<p>'El tipo de archivo no válido, espera': $0.</p>`,
    statusFileSize: `<p>'El archivo es demasiado grande, tamaño máximo de archivo': $0 MB.</p>`,
    statusNoSupport: `<p>'Su navegador no admite el recorte de imágenes'.</p>`,
    statusUnknownResponse: `<span class="slim-upload-status-icon"></span> 'Un error desconocido ocurrió'`,
    statusUploadSuccess: `<span class="slim-upload-status-icon"></span> 'Guardada'`,
    statusContentLength: `<span class="slim-upload-status-icon"></span>'El archivo es probablemente demasiado grande'`,
    meta: {}
  })