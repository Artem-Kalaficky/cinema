const addImageFormBtn = document.querySelector("#add-image-form");
const submitFormBtn = document.querySelector('[type="submit"]');
const imageForm = document.getElementsByClassName("image-form");
const mainForm = document.querySelector("#form-container");
const totalForms = document.querySelector("#id_gallery_formset-TOTAL-FORMS");

let formCount = imageForm.length-1;

addImageFormBtn.addEventListener("click", function (event) {
    event.preventDefault();
    const newImageForm = imageForm[0].cloneNode(true);
    const formRegex = RegExp(`gallery_formset-(\\d){1}-`, 'g');
    formCount++;
    newImageForm.innerHTML = newImageForm.innerHTML.replace(formRegex, `gallery_formset-${formCount}-`);
    totalForms.setAttribute('value', `${formCount + 1}`);
    mainForm.insertBefore(newImageForm, submitFormBtn);
});
