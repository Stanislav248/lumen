import re

from django import forms

from .models import Screening, Ticket

AGE_LIMITS = (0, 6, 12, 16, 18)


class ScreeningForm(forms.ModelForm):
    class Meta:
        model = Screening
        fields = ["title", "description", "genre", "hall",
                  "start_time", "price", "age_limit"]
        widgets = {
            "start_time": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
        }

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Ціна має бути більшою за нуль.")
        return price

    def clean_age_limit(self):
        age = self.cleaned_data["age_limit"]
        if age not in AGE_LIMITS:
            raise forms.ValidationError(
                "Віковий ліміт має бути одним зі значень: 0, 6, 12, 16, 18."
            )
        return age


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["client_name", "phone", "seats_count"]

    def __init__(self, *args, screening=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.screening = screening

    def clean_phone(self):
        phone = re.sub(r"[\s()\-]", "", self.cleaned_data["phone"])
        if not re.fullmatch(r"\+?\d+", phone):
            raise forms.ValidationError(
                "Телефон має містити лише цифри (допускається + на початку)."
            )
        if not 10 <= len(phone) <= 13:
            raise forms.ValidationError(
                "Телефон має містити від 10 до 13 символів."
            )
        return phone

    def clean_seats_count(self):
        count = self.cleaned_data["seats_count"]
        if count < 1:
            raise forms.ValidationError("Потрібно купити щонайменше один квиток.")
        if self.screening and count > self.screening.free_seats():
            raise forms.ValidationError(
                f"Вільних місць лише {self.screening.free_seats()}."
            )
        return count
