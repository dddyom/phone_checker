from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional

import requests
from bs4 import BeautifulSoup
from requests import Response

from app.settings import REGISTRY_URL


class RegistryLoaderException(Exception):
    pass


@dataclass
class RegistryLoader(object):
    """
    Загрузчик реестра номеров

    Указавыются при необходимости (для тестов)

    :param response: Ответ от реестра номеров
    :param parser: Объект парсера BeautifulSoup
    """

    response: Optional[Response] = None
    parser: Optional[BeautifulSoup] = None

    def __post_init__(self):

        if not str(REGISTRY_URL).strip():
            raise RegistryLoaderException("REGISTRY_URL is not set")

    def _make_request(self) -> None:
        """
        Отправка GET запроса в реестр номеров
        В случае успешного запроса сохраняет его результат в response

        :raises RegistryLoaderException: В случае ошибки при отправке запроса
        """
        try:
            self.response = requests.get(REGISTRY_URL, verify=False)

            if not self.response.status_code == HTTPStatus.OK:
                raise RegistryLoaderException("Unexpected response status code")

        except requests.exceptions.RequestException:
            raise RegistryLoaderException("Failed to call registry")

    def _init_parser(self, response: Response) -> None:
        """
        Инициализация парсера BeautifulSoup

        :param response: результат запроса к реестру номеров
        """
        self.parser = BeautifulSoup(response.content, "html.parser")

    @staticmethod
    def get_load_links(parser: BeautifulSoup) -> list[str]:
        """
        Формирование списка ссылок на csv файлы с рестром

        :param parser: парсер BeautifulSoup с загруженной страницей
        :return: Список ссылок на csv файлы
        """
        a_tags = parser.find_all("a")
        is_csv_download_link = lambda href_attr: href_attr and "downloads" in href_attr and "csv" in href_attr
        return [a.get("href") for a in a_tags if is_csv_download_link(a.get("href"))]

    def get_csv_links(self) -> list[str]:
        """
        Возвращает список ссылок на csv файлы со страницы реестра номеров

        :return: Список ссылок на csv файлы
        """
        if not self.response:
            self._make_request()

        if not self.response:
            raise RegistryLoaderException("Response is not initialized")

        if not self.parser:
            self._init_parser(self.response)

        if not self.parser:
            raise RegistryLoaderException("Parser is not initialized")
        return self.get_load_links(self.parser)
