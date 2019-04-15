// const apiKey = "AIzaSyBCawh2etNJZTS3G9t0K1O6y-MNQeK5xoY";
const createRequestWindow = document.getElementById("createRequestOpen");

// $("select").selectric();

$('#requestTime').datepicker({
    language: 'ru',
    position: 'bottom left',
    classes: 'datepicker-position',
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
    //When u select some space in the calendar do the following:
    select: function (start, end, allDay) {
        //do something when space selected
        //Show 'add event' modal
        createRequestWindow.classList.add("show");
        // document.querySelector(".request-form__date-input").value = start.format("MM-DD-YYYY");
        // document.querySelector(".request-form__start-time-input").value = start.format("HH-mm");
        // document.querySelector(".request-form__end-time-input").value = end.format("HH-mm");
        console.log(start, end, allDay);
    },
});

window.addEventListener("click", function(event) {
    if (event.target === createRequestWindow) {
        createRequestWindow.classList.remove("show");
    }
});

document.getElementById("createRequestClose").addEventListener("click", function(event) {
    createRequestWindow.classList.remove("show");
});

