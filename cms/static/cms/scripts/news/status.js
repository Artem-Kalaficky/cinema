$('#delete-picture').click(function () {
    $('#id_base_form-main_picture').val("");
    $('#picture').attr("src", "/static/cms/dist/img/preview.png")
})

$(window).keyup(function(e){
	var target = $('.checkbox-ios input:focus');
	if (e.keyCode == 9 && $(target).length){
		$(target).parent().addClass('focused');
	}
});

$('.checkbox-ios input').focusout(function(){
	$(this).parent().removeClass('focused');
});