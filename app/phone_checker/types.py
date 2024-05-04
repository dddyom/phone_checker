from enum import Enum
from typing import Any, Dict, List

CsvContent = List[Dict[str, Any]]
PhoneSearchResult = Dict[str, str]


class NumericRegistryNames(str, Enum):
    """
    Названия полей модели
    """

    CODE = "code"
    DIAPASONE_FROM = "diapasone_from"
    DIAPASONE_TO = "diapasone_to"
    CAPASITY = "capasity"
    OPERATOR = "operator"
    REGION = "region"
    ADDRESS = "address"
    INN = "inn"


# Map колонок csv с названиями полей модели
CsvHeadersIndexesMap = (
    (0, NumericRegistryNames.CODE),
    (1, NumericRegistryNames.DIAPASONE_FROM),
    (2, NumericRegistryNames.DIAPASONE_TO),
    (3, NumericRegistryNames.CAPASITY),
    (4, NumericRegistryNames.OPERATOR),
    (5, NumericRegistryNames.REGION),
    (6, NumericRegistryNames.ADDRESS),
    (7, NumericRegistryNames.INN),
)
