function valid() {
	let element = $('option[value="on"]')
	let len = element.length
	if (len == 0) {
		$('#submit-btn2').prop('disabled', false)
		return true;
	}
	$('#submit-btn2').prop('disabled', true)
		return false;
}

function preview() {
    picture.src=URL.createObjectURL(event.target.files[0]);
	img = new Image();
	img.src = URL.createObjectURL(event.target.files[0]);
	img.onload = function () {
		if (img.width == 2000 && img.height == 3000) {
			$('#valid_img').css('display', 'none').attr('value', 'off');
			valid()
			return true;
		}
		$('#valid_img').css('display', 'block').attr('value', 'on');
		valid()
		return false;
	}
}


$('#delete-picture').click(function () {
    $('#id_base_form-photo').val("");
    $('#picture').attr("src", "/static/cms/dist/img/preview.png")
	$('#valid_img').attr('value', 'off').css('display', 'none')
	valid()
})








