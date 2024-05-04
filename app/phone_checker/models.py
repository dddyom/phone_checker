from django.db import models


class NumericRegistry(models.Model):
    """
    Модель таблицы numeric_registry (Для выгрузки реестра в бд приложения)
    """

    id = models.UUIDField(primary_key=True)
    code = models.BigIntegerField(verbose_name="Code")
    diapasone_from = models.BigIntegerField(verbose_name="Diapasone From")
    diapasone_to = models.BigIntegerField(verbose_name="Diapasone To")
    capasity = models.BigIntegerField(verbose_name="Capasity")
    operator = models.CharField(max_length=500)
    region = models.CharField(max_length=1000)
    address = models.CharField(max_length=4000)
    inn = models.CharField(max_length=200, verbose_name="INN")

    class Meta:
        db_table = "numeric_registry"
