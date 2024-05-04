import re

from django import forms

from .constants import MSISDN_NUMBER_LENGTH, MSISDN_PATTERN


def validate_msisdn(value: str):
    """
    Проверка номера телефона на соответствие формату MSISDN

    :param value: значение поля
    :raises forms.ValidationError: В случае несоответствия формату
    """
    if not re.match(MSISDN_PATTERN, value):
        raise forms.ValidationError("Неверный формат. Введите номер в формате 79999999999")


class PhoneForm(forms.Form):

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите номер",
                "autocomplete": "off",
                "class": "border border-gray-300 p-2 rounded-l-md w-full focus:outline-none focus:border-blue-500",
            }
        ),
        label="Номер",
        validators=[validate_msisdn],
        required=True,
        max_length=MSISDN_NUMBER_LENGTH,
        min_length=MSISDN_NUMBER_LENGTH,
    )
