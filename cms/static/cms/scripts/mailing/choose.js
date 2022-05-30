//checkbox for choose users
$('#all_users').on('change', function () {
    if ($(this).is(':checked')) {
        $('#choose-btn').prop('disabled', true);
        return false
    }
})
$('#selective_users').on('change', function () {
    if ($(this).is(':checked')) {
        $('#choose-btn').prop('disabled', false);
    }
})

//preview name.html
$('#id_file_form-letter').on('change', function() {
  let splittedFakePath = this.value.split('\\');
  $('#loaded_template').text(splittedFakePath[splittedFakePath.length - 1]);
  $('#current_template').text(splittedFakePath[splittedFakePath.length - 1]);
  $('.radio-unchecked').prop('checked', false)
});

//submit
$('#go').on('click', function () {
    $('#mailing-form').submit();
})

//checked email
function checked_email(index) {
    $('#id_file_form-letter')[0].value= "";
    $('#loaded_template').text('');
    if ($('#' + index).is(':checked')) {
        let name = $('#name' + index).text();
        $('#current_template').text(name)
    }
}