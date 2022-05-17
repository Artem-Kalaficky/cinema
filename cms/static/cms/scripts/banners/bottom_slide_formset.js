$('#add_more1').click(function() {
	var form_idx1 = $('#id_bottom_carousel_formset-TOTAL_FORMS').val();
	$('#form_set1').append($('#empty_form1').html().replace(/__prefix__/g, form_idx1));
	$('#id_bottom_carousel_formset-TOTAL_FORMS').val(parseInt(form_idx1) + 1);
});

function is_valid1() {
	let $elements1 = $('option[value="on"]')
	let len1 = $elements1.length
	if (len1 == 0) {
		$('#submit-btn1').prop('disabled', false)
		return true;
	}
	$('#submit-btn1').prop('disabled', true)
		return false;
}

function delete_image1(index) {
	$('#id_' + index + '-image1').val("");
	$('.delete-list1').append('<input type="hidden" value="on" name="' + index  + '-DELETE" id="id_' + index + '-DELETE">');
	$('#' + index + '-form1').css('display', 'none');
	$('#' + index + '-validation1').attr('value', 'off')
	is_valid1()
}

function preview_gallery1(index) {
	$('#' + index + '-image1').attr('src', URL.createObjectURL(event.target.files[0]));
	img1 = new Image();
	img1.src = URL.createObjectURL(event.target.files[0]);
	img1.onload = function () {
		if (img1.width == 1000 && img1.height == 190) {
			$('#' + index + '-validation1').css('display', 'none').attr('value', 'off');
			is_valid1()
			return true;
		}
		$('#' + index + '-validation1').css('display', 'inline-block').attr('value', 'on');
		is_valid1()
		return false;
	}
}