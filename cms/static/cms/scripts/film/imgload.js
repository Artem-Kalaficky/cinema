function preview() {
    picture.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-picture').click(function () {
    $('#id_base_form-picture').val("");
    $('#picture').attr("src", "/static/cms/dist/img/preview.png")
})



