function preview_scheme() {
    scheme.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-scheme').click(function () {
    $('#id_base_form-scheme').val("");
    $('#scheme').attr("src", "/static/cms/dist/img/preview.png")
})

function preview_banner() {
    banner.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-banner').click(function () {
    $('#id_base_form-top_banner').val("");
    $('#banner').attr("src", "/static/cms/dist/img/preview.png")
})