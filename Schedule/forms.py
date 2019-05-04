from django import forms
from .models import Project, Request


class RequestForm(forms.Form):

    CHOICES = (
        ("equipment1", "Обладнання1"),
        ("equipment2", "Обладнання2"),
        ("equipment3", "Обладнання3"),
        ("equipment4", "Обладнання4"),)
    time = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        "class": "input-wrap__input datepicker-here", "data-range": "true", "data-multiple-dates-separator": " - ",
        "data-timepicker": "true", "id": "requestTime", "autocomplete": "off", }))
    equipment = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.Select(attrs={
        "id": "requestEquip", "class": "input-wrap__input", }))
    description = forms.CharField(required=True, max_length=600, widget=forms.Textarea(attrs={
        "class": "input-wrap__input", "id": "requestDesc", "cols": "30", "rows": "10", }))

    def __init__(self, *args, **kwargs):
        self.service = kwargs.pop("service", None)
        super(RequestForm, self).__init__(*args, **kwargs)

    def clean(self):
        calendar_id = "1ga5hvcp7huhrh26vpa88qsf84@group.calendar.google.com"
        equipment = self.cleaned_data["equipment"]
        start, end = self.cleaned_data["time"].split(" - ")
        start_date, start_time = start.split()
        end_date, end_time = end.split()
        related_events = self.service.events().list(calendarId=calendar_id,
                                                    timeMin="{}T{}:00+03:00".format(start_date, start_time),
                                                    timeMax="{}T{}:00+03:00".format(end_date, end_time)).execute()
        for event in related_events["items"]:
            print(event["summary"])
            print(equipment)
            print(equipment == event["summary"])
            if equipment == event["summary"]:
                print("error")
                raise forms.ValidationError("Нажаль, на заданий період обладнання вже заброньоване. Будь ласка оберіть інший час.")
        return self.cleaned_data

    def save(self):
        event_body = RequestForm.get_event_body(self.cleaned_data["time"], self.cleaned_data["equipment"], self.cleaned_data["description"])
        event = self.service.events().insert(calendarId='primary', body=event_body).execute()
        print("Request send seccessfully")
        print('Event created: %s' % (event.get("htmlLink")))

    @staticmethod
    def get_event_body(time, equipment, description):
        calendar_id = '1ga5hvcp7huhrh26vpa88qsf84@group.calendar.google.com'
        start, end = time.split(" - ")
        start_date, start_time = start.split()
        end_date, end_time = end.split()
        print(start_date, start_time, end_date, end_time)
        event = {
            'summary': '{}'.format(equipment),
            'description': '{}'.format(description),
            'start': {
                'dateTime': '{}T{}:00'.format(start_date, start_time),
                'timeZone': 'Europe/Kiev',
            },
            'end': {
                'dateTime': '{}T{}:00'.format(end_date, end_time),
                'timeZone': 'Europe/Kiev',
            },
            'attendees': [
                {'email': calendar_id},
            ],
        }
        return event


class CreateProjectForm(forms.Form):
    title = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        "class": "input-wrap__input", "id": "projectTitle", }))
    description = forms.CharField(required=True, max_length=600, widget=forms.Textarea(attrs={
        "class": "input-wrap__input", "id": "projectDesc", "cols": "30", "rows": "10", }))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(CreateProjectForm, self).__init__(*args, **kwargs)

    def clean(self):
        title = self.cleaned_data["title"]
        if Request.objects.filter(title=title).exists() or Project.objects.filter(title=title).exists():
            print("error")
            raise forms.ValidationError("Проект або заявка з введеной назвою все існує. Будь ласка введіть іншу назву.")
        return self.cleaned_data

    def save(self):
        print("Request send seccessfully")
        Request.objects.create(admin=self.user, title=self.cleaned_data["title"], description=self.cleaned_data["description"])



