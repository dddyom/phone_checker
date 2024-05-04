from django.urls import path

from .views import phone_form

urlpatterns = [
    path("", phone_form, name="phone_form"),
]
