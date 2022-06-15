//variables for concrete filters
let cinema_id = new Map()
let date = new Map()
let type_all = new Map()
let d2 = new Map()
let d3 = new Map()
let imax = new Map()

//fill default data
cinema_id.set('cinema_id', false)
type_all.set('type_all', true)
d2.set('2d', false)
d3.set('3d', false)
imax.set('imax', false)

//variables for type-button
let type_2d = $('#2d')
let type_3d = $('#3d')
let type_imax = $('#imax')
let type_All = $('#all')


//get data from type filters
$(type_2d).click(function (){
    $(this).addClass('btn-dark').removeClass('btn-outline-dark')
    $(type_3d).removeClass('btn-dark').addClass('btn-outline-dark')
    $(type_imax).removeClass('btn-dark').addClass('btn-outline-dark')
    $(type_All).removeClass('btn-dark').addClass('btn-outline-dark')
    d2.set('2d', true)
    d3.set('3d', false)
    imax.set('imax', false)
    type_all.set('type_all', false)
    get_data()
})

$(type_3d).click(function (){
    $(this).addClass('btn-dark').removeClass('btn-outline-dark')
    $(type_2d).removeClass('btn-dark').addClass('btn-outline-dark')
    $(type_imax).removeClass('btn-dark').addClass('btn-outline-dark')
    $(type_All).removeClass('btn-dark').addClass('btn-outline-dark')
    d3.set('3d', true)
    d2.set('2d', false)
    imax.set('imax', false)
    type_all.set('type_all', false)
    get_data()
})

$(type_imax).click(function (){
    $(this).addClass('btn-dark').removeClass('btn-outline-dark')
    $(type_2d).removeClass('btn-dark').addClass('btn-outline-dark')
    $(type_3d).removeClass('btn-dark').addClass('btn-outline-dark')
    $(type_All).removeClass('btn-dark').addClass('btn-outline-dark')
    imax.set('imax', true)
    d2.set('2d', false)
    d3.set('3d', false)
    type_all.set('type_all', false)
    get_data()
})

$(type_All).click(function (){
    $(this).addClass('btn-dark').removeClass('btn-outline-dark')
    $(type_2d).removeClass('btn-dark').addClass('btn-outline-dark')
    $(type_3d).removeClass('btn-dark').addClass('btn-outline-dark')
    $(type_imax).removeClass('btn-dark').addClass('btn-outline-dark')
    type_all.set('type_all', true)
    d2.set('2d', false)
    d3.set('3d', false)
    imax.set('imax', false)
    get_data()
})

$('#cinema').on('change', function() {
    $('#name_cinema').html($('#cinema option:selected').text())
    if ($(this).val() !== 'all') {
        cinema_id.set('cinema_id', $(this).val())
    } else {
        cinema_id.set('cinema_id', false)
    }
    get_data()
})

function get_date(index){
    date.set('date', $('#' + index).val())
    get_data()
}