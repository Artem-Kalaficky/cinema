$('#add_more').click(function() {
	var form_idx = $('#id_gallery_formset-TOTAL_FORMS').val();
	$('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
	$('#id_gallery_formset-TOTAL_FORMS').val(parseInt(form_idx) + 1);
});


function delete_image(index) {
	$('#id_' + index + '-image')[0].value="";
	$('.delete-list').append('<input type="hidden" value="on" name="' + index  + '-DELETE" id="id_' + index + '-DELETE">');
};

function preview_gallery() {
    gallery_picture.src=URL.createObjectURL(event.target.files[0]);
}





