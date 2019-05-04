(function () {
    const createRequestWindow = document.getElementById("createRequestOpen");
    const createRequestForm = document.forms["createRequestForm"];
    const createRequestFormInputs = document.querySelectorAll('.input-wrap__input');
    const requestFormErrors = document.getElementById('createRequestFormErrors');
    const notifyMessage = document.getElementById('notifyMessage');

    console.log(createRequestForm);
    console.log(createRequestFormInputs);

    window.addEventListener("click", function(event) {
        if (event.target === createRequestWindow) {
            createRequestWindow.classList.remove("show");
        }
    });

    document.getElementById("createRequestClose").addEventListener("click", function() {
        createRequestWindow.classList.remove("show");
    });



    $('#requestTime').datepicker({
        language: {
            days: ['Неділя', 'Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця', 'Субота'],
            daysShort: ['НД', 'ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ'],
            daysMin: ['НД', 'ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ'],
            months: ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад','Грудень'],
            monthsShort: ['Сiч', 'Лют', 'Бер', 'Квiт', 'Трав', 'Черв', 'Лип', 'Серп', 'Вер', 'Жовт', 'Лист', 'Груд'],
            today: 'Сьогодні',
            clear: 'Очистити',
            dateFormat: 'yyyy-mm-dd',
            timeFormat: 'hh:ii',
            firstDay: 1,
        },
        toggleSelected: false,
        position: 'bottom right',
        classes: 'datepicker-position',
    });

    createRequestForm.elements['time'].addEventListener('keydown', function (event) {
        event.preventDefault();
    });


    $('#calendar').fullCalendar({
        googleCalendarApiKey: "AIzaSyBCawh2etNJZTS3G9t0K1O6y-MNQeK5xoY",
        eventSources: [
            {

                googleCalendarId: '1ga5hvcp7huhrh26vpa88qsf84@group.calendar.google.com',
            },
        ],
        customButtons: {
            createRequestButton: {
                text: 'Створити заявку',
                click: function() {

                    createRequestWindow.classList.add("show");
                }
            }
            },
        locale: "uk",
        defaultView: "agendaWeek",
        allDaySlot: false,
        slotDuration: "00:30",
        height: "parent",
        header: {
            left:   'today createRequestButton prev,next title',
            center: '',
            right:  'month agendaWeek agendaDay',
        },
        events: [],
        editable: true,
        selectable: true,
        timezone: "Europe/Kiev",
        select: function (start, end, allDay) {
            createRequestWindow.classList.add("show");
            createRequestForm.elements['time'].value = start.format('YYYY-MM-DD HH:mm') + ' - ' + end.format('YYYY-MM-DD HH:mm');
            console.log(start, end, allDay);
            },
    });

    if (requestFormErrors) {
        createRequestWindow.classList.add("show");
    }
    if (notifyMessage) {
        setTimeout(function () {
            notifyMessage.classList.add('notify_hide');
        }, 5000);
    }

})();


// (function () {
//     for (var input of createRequestFormInputs) {
//         console.log(input.nodeName + ': ' + input.value);
//         input.setCustomValidity('');
//         checkEmptyInput(input);
//         if (input.name === 'time') {
//             checkDateFormat(input);
//         }
//     }
// })();


// createRequestForm.addEventListener('submit', function (event) {
//     event.preventDefault();
//     for (var input of createRequestFormInputs) {
//         if (input.value === '') {
//             input.setCustomValidity("Обов'язкове поле");
//             //this.elements['submit'].click();
//             console.log('submit');
//         }
//         else {
//             input.setCustomValidity('');
//         }
//     }
//     createRequestForm.submit();
// });


// function checkEmptyInput(input) {
//     input.addEventListener('keyup', function () {
//         if (this.value === '') {
//             this.setCustomValidity("Обов'язкове поле");
//             createRequestForm.elements['submit'].click();
//             this.focus();
//         }
//         else {
//             this.setCustomValidity('');
//         }
//     });
// }

// function checkDateFormat(input) {
//     input.addEventListener('keyup', function () {
//
//         var isValidDateFormat = input.value.match('/^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])\s(0[1-9]|1[0-9]|2[0-3])]\:(0[0-9]|[12345][]|)\s\-\sd{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])s(0[1-9]|1[0-9]|2[0-3])$/');
//         console.log(input.value.split(' - '));
//         if (!isValidDateFormat) {
//             input.setCustomValidity('Поле дати має відповідати формату YYYY-MM-DD HH:II - YYYY-MM-DD HH:II');
//             createRequestForm.elements['submit'].click();
//             input.focus();
//         }
//         else {
//             input.setCustomValidity('');
//         }
//
//         this.setCustomValidity();
//         createRequestForm.elements['submit'].click();
//         input.focus();
//     });
// }






