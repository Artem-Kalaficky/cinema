let collect_data = new Map()
//init DataTable
$(function () {
    $("#example").DataTable({
        "responsive": false,
        "lengthChange": false,
        "autoWidth": false,
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
    })
});


//checkbox for choice All users or Selective choice users
let sumOfAllUsers = $('.user_email').length
$('#all_users').on('change', function () {
    if ($(this).is(':checked')) {
        $('#sum_letter').text(sumOfAllUsers);
        $('#choose-btn').prop('disabled', true);
        collect_data.set('emails', $("#example").DataTable().data().pluck(4).toArray())
    }
});
$('#selective_users').on('change', function () {
    if ($(this).is(':checked')) {
        $('#choose-btn').prop('disabled', false);
        $('.checked_user', $("#example").DataTable().rows().nodes()).prop('checked', false).removeClass('check-true');
        $('#sum_letter').text(0);
        collect_data.delete('emails')
    }
});


//count selective letter and emails
$('.btn-close, .btn-close-send').on('click', function () {
    let count = $('.check-true', $("#example").DataTable().rows().nodes()).length;
    $('#sum_letter').text(count);
    data = $("#example").DataTable().rows(function (idx, data, node) {
        return $(node).find('input[type="checkbox"]').prop('checked');
    }).data().pluck(4).toArray()
    collect_data.set('emails', data)
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


//check of choose current 5 emails
function checked_email(index) {
    $('#id_file_form-letter')[0].value= "";
    $('#loaded_template').text('');
    if ($('#' + index).is(':checked')) {
        let name = $('#name' + index).text();
        let id = $('#id' + index).text();
        $('#current_template').text(name);
        collect_data.set('id_template', id)
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


//get html file
$('input[type=file]').on('change', function () {
    let file = this.files[0]
    collect_data.set('file', file)
})


//csrf
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


