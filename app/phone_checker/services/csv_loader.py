from dataclasses import dataclass
from http import HTTPStatus
from io import StringIO

import pandas as pd
import requests
from phone_checker.types import CsvContent, CsvHeadersIndexesMap


class CsvLoaderException(Exception):
    pass


@dataclass
class CsvLoader(object):
    """
    Загрузка csv файлов с реестром номеров

    :param links: Ссылки на csv файлы
    """

    links: list[str]

    def get_response_content(self, link: str) -> str:
        """
        Отправка GET запроса в реестр номеров
        В случае успешного запроса сохраняет его результат в response

        :raises RegistryLoaderException: В случае ошибки при отправке запроса
        """
        try:
            response = requests.get(link, verify=False)

            if not response.status_code == HTTPStatus.OK:
                raise CsvLoaderException("Unexpected response status code")

            return response.content.decode("utf-8")

        except requests.exceptions.RequestException:
            raise CsvLoaderException("Failed to load csv")

    def _get_local_df(self, content: str) -> pd.DataFrame:
        """
        Формирование DataFrame с csv файлом из одного запроса

        :param content: контент запроса
        :return: DataFrame с csv файлом
        """
        df = pd.read_csv(StringIO(content), delimiter=";", quotechar='"')
        df.rename(columns={df.columns[index]: name.value for index, name in CsvHeadersIndexesMap}, inplace=True)
        return df

    def get_df(self) -> pd.DataFrame:
        """
        Формирование DataFrame с результатами всех csv

        :return: DataFrame со всеми csv
        """
        dfs = [self._get_local_df(content=self.get_response_content(link)) for link in self.links]
        return pd.concat(dfs, ignore_index=True)

    def get_numeric_registry_list(self) -> CsvContent:
        """
        Формирование списка словарй с данными из реестра

        :return: Содержимое всех csv в списке словарей
        """
        df = self.get_df()

        df.to_csv("concatenated_data.csv", index=False)
        return df.to_dict(orient="records")
