from typing import List
from uuid import uuid4

from celery import shared_task
from django.db import transaction

from .models import NumericRegistry
from .services import CsvLoader, RegistryLoader


@shared_task
def load_numeric_registry():
    """
    Задача для выгрузки реестра в бд приложения
    """
    csv_links: List[str] = RegistryLoader().get_csv_links()

    numeric_registry_instances = [
        NumericRegistry(
            str(uuid4()),
            row.get("code"),
            row.get("diapasone_from"),
            row.get("diapasone_to"),
            row.get("capasity"),
            row.get("operator"),
            row.get("region"),
            row.get("address"),
            row.get("inn"),
        )
        for row in CsvLoader(links=csv_links).get_numeric_registry_list()
    ]

    with transaction.atomic():
        NumericRegistry.objects.all().delete()
        NumericRegistry.objects.bulk_create(numeric_registry_instances)
