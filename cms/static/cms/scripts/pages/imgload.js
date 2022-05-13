function preview_logo() {
    logo.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-logo').click(function () {
    $('#id_base_form-logo').val("");
    $('#logo').attr("src", "/static/cms/dist/img/preview.png")
})