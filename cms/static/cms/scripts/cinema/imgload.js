function preview_logo() {
    logo.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-logo').click(function () {
    $('#id_base_form-logo').val("");
    $('#logo').attr("src", "/static/cms/dist/img/preview.png")
})

function preview_banner() {
    banner.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-banner').click(function () {
    $('#id_base_form-top_banner').val("");
    $('#banner').attr("src", "/static/cms/dist/img/preview.png")
})