$('#languages').on('change', function () {
    localStorage.removeItem('film_name')
    localStorage.removeItem('cinema_id')
    this.form.submit();
});