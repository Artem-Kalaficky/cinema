//init DataTable
 $(function () {
    let table = $("#example").DataTable({
        "responsive": false,
        "lengthChange": false,
        "autoWidth": true,
        "language": {
            "infoFiltered": "(Отфильтровано _MAX_ записей)",
            "zeroRecords": "Записей не найдено",
            "info": "Показано с _START_ по _END_ записей из _TOTAL_",
            "infoEmpty": "Нет записей.",
            "search": "Поиск:",
            "paginate": {
                "previous": "Предыдущая",
                "last": "Последняя",
                "next": "Следующая"
            }
        }
    });
    //count selective users
    $('.btn-close').on('click', function () {
        let count = $('.check-true', table.rows().nodes()).length
        $('#sum_letter').text(count)
    })
});


//checkbox for choice All users or Selective choice users
let sumOfLetterAll = $('.user_email').length
$('#all_users').on('change', function () {
    if ($(this).is(':checked')) {
        $('#sum_letter').text(sumOfLetterAll)
        $('#choose-btn').prop('disabled', true);
        return false;
    }
});
$('#selective_users').on('change', function () {
    if ($(this).is(':checked')) {
        $('#choose-btn').prop('disabled', false);
        $('.checked_user', $("#example").DataTable().rows().nodes()).prop('checked', false).removeClass('check-true');
        $('#sum_letter').text(0)
    }
});


//preview name of loaded file .html
$('#id_file_form-letter').on('change', function() {
  let splittedFakePath = this.value.split('\\');
  $('#loaded_template').text(splittedFakePath[splittedFakePath.length - 1]);
  $('#current_template').text(splittedFakePath[splittedFakePath.length - 1]);
  $('.radio-unchecked').prop('checked', false);
  //validation of extend .html
  let fileExt = ['html'];
  let parts = $(this).val().split('.');
  if(fileExt.join().search(parts[parts.length - 1]) != -1){
      $('#errorext').css('display', 'none');
      $('#go').prop('disabled', false);
    } else {
      $('#errorext').css('display', 'block');
      $('#go').prop('disabled', true);
    }
});


//submit and mailing
$('#go').on('click', function () {
    $('#mailing-form').submit();
});


//check of choose current 5 emails
function checked_email(index) {
    $('#id_file_form-letter')[0].value= "";
    $('#loaded_template').text('');
    if ($('#' + index).is(':checked')) {
        let name = $('#name' + index).text();
        $('#current_template').text(name);
    }
}


//choose users in DataTable
$('.checked_user').on('change', function () {
    if ($(this).is(':checked')) {
        $(this).addClass('check-true');
    } else {
        $(this).removeClass('check-true');
    }
});

