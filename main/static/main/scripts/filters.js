//variables for concrete filters
let cinema_id = new Map()
let hall_id = new Map()
let film = new Map()
let date = new Map()
let d2 = new Map()
let d3 = new Map()
let imax = new Map()

//fill default data
cinema_id.set('cinema_id', localStorage.cinema_id)
$(function (){
    $('.selected-cinema').each(function (value){
        if ($('#cinema-' + value).val() === localStorage.cinema_id){
            $('#cinema-' + value).prop('selected', true)
        }
    })
})

film.set('film', localStorage.film_name)
$(function (){
    $('.selected-film').each(function (value){
        if ($('#film-' + value).val() === localStorage.film_name){
            $('#film-' + value).prop('selected', true)
        }
    })
})

hall_id.set('hall_id', false)
d2.set('2d', true)
d3.set('3d', true)
imax.set('imax', true)



//first select
function first_select(){
    $('#table').css('display', 'none')
    $('#table1').css('display', 'block')
    $("#table1 tbody td").remove()
}

//get cinema filter data
$('#cinema').on('change', function() {
    localStorage.removeItem('cinema_id')
    if ($(this).val() !== 'all') {
        cinema_id.set('cinema_id', $(this).val())
        hall_id.set('hall_id', false)
    } else {
        cinema_id.set('cinema_id', false)
        hall_id.set('hall_id', false)
    }
    $('.hall-option').remove()
    get_data_cinema()
})

//get hall filter data
$('#select-halls').on('change', function() {
    if ($(this).val() !== 'all') {
        hall_id.set('hall_id', $(this).val())
    } else {
        hall_id.set('hall_id', false)
    }
    get_data()
})

//get film filter data
$('#film').on('change', function() {
    localStorage.removeItem('film_name')
    if ($(this).val() !== 'all') {
        film.set('film', $(this).val())
    } else {
        film.set('film', false)
    }
    get_data()
})

//get date filter data
$('#date').on('change', function() {
    date.set('date', $(this).val())
    get_data()
})

//get type2d filter data
$('#2d').on('change', function() {
    d2.set('2d', $(this).is(':checked'))
    get_data()
})

//get type3d filter data
$('#3d').on('change', function() {
    d3.set('3d', $(this).is(':checked'))
    get_data()
})

//get type-imax filter data
$('#imax').on('change', function() {
    imax.set('imax', $(this).is(':checked'))
    get_data()
})







