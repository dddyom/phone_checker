from http import HTTPStatus

from django.http import HttpRequest, HttpResponse


def handler_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    return HttpResponse("Page not found".encode(), status=HTTPStatus.NOT_FOUND)
