from dataclasses import dataclass
from typing import Dict, Literal, Tuple, Union

from phone_checker.constants import MSISDN_NUMBER_LENGTH
from phone_checker.models import NumericRegistry
from phone_checker.types import PhoneSearchResult


class PhoneSearcherException(Exception):
    pass


@dataclass
class PhoneSearcher:
    """
    Поиск номера в реестре

    :param phone: номер телефона в формате MSISDN
    """

    phone: str

    def parse_phone(self) -> Tuple[int, int]:
        """
        Разбивает номер телефона на код и номер для поиска в диапазоне

        :raises PhoneSearcherException: При несоответствии длины номера
        :return: code, number
        """
        if len(self.phone) != MSISDN_NUMBER_LENGTH:
            raise PhoneSearcherException(f"Phone must be {MSISDN_NUMBER_LENGTH} digits long")
        return int(self.phone[1:4]), int(self.phone[4:])

    def _find_in_registry(self, code: int, number: int) -> PhoneSearchResult:
        """
        Запрос для поска в реестре

        :param code: код (первые три цифры в номере телефона)
        :param number: последние 7 цифр в номере телфона (для поиска в диапазоне)
        :return: оператор, регион и адрес для введеного номера
        """
        return (
            NumericRegistry.objects.filter(code=code, diapasone_from__lte=number, diapasone_to__gte=number)
            .values("operator", "region", "address")
            .first()
        )

    def _load(self) -> PhoneSearchResult:
        """
        Запуск парсера номера телефона и его поиск по реестру

        :return: оператор, регион и адрес для введеного номера
        """
        code, number = self.parse_phone()

        return self._find_in_registry(code, number)

    def get_cleaned_results(
        self,
    ) -> Dict[Literal["result", "error", "is_not_found"], Union[PhoneSearchResult, str, bool]]:
        """

        :return: оператор, регион и адрес для введеного номера
        """
        try:
            found = self._load()
            return {"result": found, "error": "", "is_not_found": not bool(found)}
        except PhoneSearcherException as e:
            return {"result": {}, "error": str(e), "is_not_found": True}
