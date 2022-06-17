//set variables
let cost = parseInt($('#cost').text())
let collect_data = new Map()


//get row and place
function get_place_list() {
    let list = $('.selected').map(function (){
        return $(this).attr('place')
    })
    collect_data.set('place_list', list.toArray())
}

function get_row_list() {
    let list = $('.selected').map(function (){
        return $(this).attr('row')
    })
    collect_data.set('row_list', list.toArray())
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
    block_btn()
    $('#num_tickets').html($('.selected').length)
    $('.num_cost').html($('.selected').length * cost)
})


//reserve or buy tickets
function create_ticket() {
    block_btn()
    get_place_list()
    get_row_list()
    $('.selected').addClass('reserve').removeClass('selected').attr('fill', 'grey')
    $('#numb-reserved').html($('.reserve').length)
    $('#num_tickets').html(0)
    $('.num_cost').html(0)
    get_tickets()
    collect_data.delete('place_list')
    collect_data.delete('row_list')
    collect_data.delete('status')
    console.log(collect_data)
    $('.reserve').unbind('click');
    setTimeout(block_btn(), 100)
}
$('.reserve-btn').click(function (){
    if ($('.selected').length !== 0) {
        collect_data.set('status', false)
        create_ticket()
    } else {
        $('#error').css('display', 'block')
        setTimeout(function (){
            $('#error').css('display', 'none')
        }, 3000)
    }
})

$('#buy').click(function (){
    if ($('.selected').length !== 0) {
        collect_data.set('status', true)
        create_ticket()
    } else {
        $('#error').css('display', 'block')
        setTimeout(function (){
            $('#error').css('display', 'none')
        }, 3000)
    }
})

function block_btn(){
    if ($('.selected').length === 0) {
        $('#for-buy').prop('disabled', true)
    } else {
        $('#for-buy').prop('disabled', false)
    }
}
block_btn()









