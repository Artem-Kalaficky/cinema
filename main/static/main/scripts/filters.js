//all data of choose filters
let filter_data = new Map()

//variables for concrete filters
let cinema_id = new Map()
let hall_id = new Map()
let film = new Map()
let date = new Map()
let d2 = new Map()
let d3 = new Map()
let imax = new Map()
d2.set('2d', $('#2d').is(':checked'))
d3.set('3d', $('#3d').is(':checked'))
imax.set('imax', $('#imax').is(':checked'))

//first select
function first_select(){
    $('#table').css('display', 'none')
    $('#table1').css('display', 'block')
    $("#table1 tbody td").remove()
}

//get cinema filter data
$('#cinema').on('change', function() {
    if ($(this).val() !== 'all') {
        cinema_id.set('cinema_id', $(this).val())
    } else {
        cinema_id.set('cinema_id', false)
    }
    $('.hall-option').remove()
    first_select()
    get_data_cinema()
})

//get hall filter data
$('#select-halls').on('change', function() {
    hall_id.set('hall_id', $(this).val())
    first_select()
    get_data()
})

//get film filter data
$('#film').on('change', function() {
    film.set('film', $(this).val())
    first_select()
    get_data()
})

//get date filter data
$('#date').on('change', function() {
    date.set('date', $(this).val())
    first_select()
    get_data()
})

//get type2d filter data
$('#2d').on('change', function() {
    d2.set('2d', $(this).is(':checked'))
    first_select()
    get_data()
})

//get type3d filter data
$('#3d').on('change', function() {
    d3.set('3d', $(this).is(':checked'))
    first_select()
    get_data()
})

//get type-imax filter data
$('#imax').on('change', function() {
    imax.set('imax', $(this).is(':checked'))
    first_select()
    get_data()
})


