# Generated by Django 5.0.4 on 2024-05-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("phone_checker", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="numericregistry",
            name="capasity",
            field=models.BigIntegerField(verbose_name="Capasity"),
        ),
        migrations.AlterField(
            model_name="numericregistry",
            name="code",
            field=models.BigIntegerField(verbose_name="Code"),
        ),
        migrations.AlterField(
            model_name="numericregistry",
            name="diapasone_from",
            field=models.BigIntegerField(verbose_name="Diapasone From"),
        ),
        migrations.AlterField(
            model_name="numericregistry",
            name="diapasone_to",
            field=models.BigIntegerField(verbose_name="Diapasone To"),
        ),
    ]
