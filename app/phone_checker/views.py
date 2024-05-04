from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import PhoneForm
from .services import PhoneSearcher


def phone_form(request: HttpRequest) -> HttpResponse:
    template_name = "phone_checker/phone_form.tpl.html"
    form = PhoneForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            return render(
                request, template_name, {"form": form} | PhoneSearcher(form.cleaned_data["phone"]).get_cleaned_results()
            )

    return render(request, template_name, {"form": form})
