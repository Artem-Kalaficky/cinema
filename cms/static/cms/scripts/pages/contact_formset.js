$('#add_more').click(function() {
	var form_idx = $('#id_contact_formset-TOTAL_FORMS').val();
	$('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
	$('#id_contact_formset-TOTAL_FORMS').val(parseInt(form_idx) + 1);
});


function preview_logo(index) {
    let url = URL.createObjectURL(event.target.files[0]);
    $('#' + index + '-image').attr('src', url)
}

function delete_logo(index) {
    $('#id_' + index + '-logo').val("");
    $('#' + index + '-image').attr('src', "/static/cms/dist/img/preview.png")
}
