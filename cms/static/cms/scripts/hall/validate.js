$('form').submit(function () {
    if (($('#id_base_form-description_uk').val().length<1)) {
        $('.card').css('display', 'flex');
        $('body,html').animate({scrollTop: 0}, 200);
        setTimeout(function (){
            $('.card').css('display', 'none');
        },5000)
        return false
    }
    return true
})

