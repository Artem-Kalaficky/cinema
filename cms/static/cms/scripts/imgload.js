function preview() {
    picture.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-picture').click(function () {
    $('#id_base_form-main_picture').val("");
    $('#picture').attr("src", "/static/cms/dist/img/preview.png")
})


var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})


