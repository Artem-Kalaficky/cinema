let galleryFormset = document.querySelectorAll(".gallery-formset")
let formContainer = document.querySelector("#form-container")
let addButton = document.querySelector("#add-form")
let totalForms = document.querySelector("#id_gallery_formset-TOTAL_FORMS")

let formNum = galleryFormset.length-1
addButton.addEventListener('click', addForm)

function addForm(e) {
    e.preventDefault()

    let newForm = galleryFormset[0].cloneNode(true)
    let formRegex = RegExp(`gallery_formset-(\\d){1}-`,'g')

    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `gallery_formset-${formNum}-`)
    formContainer.insertBefore(newForm, addButton)

    totalForms.setAttribute('value', `${formNum+1}`)
}