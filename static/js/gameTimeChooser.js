document.addEventListener('DOMContentLoaded', function () {
    let elems = document.querySelectorAll('.timepicker');
    options = {
        'twelveHour': false,
        'i18n': {
            'done': 'Ок',
            'cancel': 'Отменить'
        }
    }
    M.Timepicker.init(elems, options);
});
