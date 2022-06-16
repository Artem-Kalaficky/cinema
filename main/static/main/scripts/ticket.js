//set variables
let cost = parseInt($('#cost').text())
let collect_data = new Map()


//get row and place
function get_place_list() {
    let list = $('.selected').map(function (){
        return $(this).attr('place')
    })
    let s = []
    $(list).each(function (value, obj){
        s[value] = obj
    })
    console.log(typeof(s))
    collect_data.set('place_list', s)
}

function get_row_list() {
    let list = $('.selected').map(function (){
        return $(this).attr('row')
    })
    collect_data.set('row_list', list)
}


//choose place
$('.unselected').click(function (){
    $(this).toggleClass('unselected').toggleClass('selected')
})

$('.selected').click(function (){
    $(this).toggleClass('selected').toggleClass('unselected')
})


//count cost and ticket
$('.part').click(function (){
    $('#num_tickets').html($('.selected').length)
    $('#num_cost').html($('.selected').length * cost)
})


//reserve or buy tickets
$('#reserve').click(function (){
    if ($('.selected').length !== 0) {
        get_place_list()
        get_row_list()
        collect_data.set('status', false)
        $('.selected').addClass('reserve').removeClass('selected').attr('fill', 'grey')
        $('#numb-reserved').html($('.reserve').length)
        $('#num_tickets').html(0)
        $('#num_cost').html(0)
        get_tickets()
        $('.reserve').unbind('click');
    } else {
        $('#error').css('display', 'block')
        setTimeout(function (){
            $('#error').css('display', 'none')
        }, 3000)
    }
})

$('#buy').click(function (){
    if ($('.selected').length !== 0) {

    } else {
        $('#error').css('display', 'block')
        setTimeout(function (){
            $('#error').css('display', 'none')
        }, 3000)
    }
})




